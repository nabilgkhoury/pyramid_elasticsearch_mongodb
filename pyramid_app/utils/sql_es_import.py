#!/usr/bin/env python -m

from typing import List, Dict
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, ResultProxy
from sqlalchemy.exc import SQLAlchemyError, ProgrammingError

from elasticsearch2 import Elasticsearch


# mysql connection string to crunshbase database
SQL_CONNECT = "mysql://mysql-service/crunshbase"
# es connection
ES_CONNECT = (dict(host='es-service', port=9200),)
ES_INDEX = 'crunshbase'


# sql statement to select top-<limit> companies with most workers
CMPS_SELECT = """
SELECT 
  o.id AS `company_id`,
  o.name AS `company_name`, 
  o.homepage_url AS `homepage_url`,
  o.logo_url AS `logo_url`,
  o.founded_at AS `founded_date`,  
  o.country_code AS `country`,  
  o.category_code AS `industry`, 
  CONCAT_WS(', ', o.city, o.region, o.state_code, o.country_code) AS `location`, 
  o.relationships AS `worker_count`
FROM cb_objects o
WHERE o.entity_type = "Company"
ORDER BY o.relationships DESC
LIMIT {limit}
"""
# sql statement to select milestones for given company <company_id>
EVENTS_SELECT = """
SELECT
        m.milestone_at AS event_date,
        m.milestone_code AS event_code,
        m.description AS event_desc,
        m.source_url AS event_url
FROM  cb_milestones m
WHERE m.object_id = '{company_id}'
"""


class SQLToESImporter(object):
    company_count: int
    companies_select: str
    sql_engine: Engine
    es_client: Elasticsearch
    es_index: str
    insertions: int

    def __init__(self,
                 company_count: int = 100,
                 cb_connect: str = SQL_CONNECT,
                 es_connect: List[Dict] = ES_CONNECT,
                 es_index: str = ES_INDEX):
        self.company_count = company_count
        # prep company selection select top-<limit> companies with most workers
        self.companies_select = CMPS_SELECT.format(limit=self.company_count)
        # connect to mysql crunshbase database
        self.sql_engine = create_engine(cb_connect)
        # connect to es instance
        self.es_client = Elasticsearch(list(es_connect))
        self.es_index = es_index
        self.insertions = 0
        if not self.es_client.ping():
            raise ValueError("ElasticSearch Ping Failed")

    def pull(self) -> Dict:
        companies_result: ResultProxy
        try:
            with self.sql_engine.connect() as conn:
                companies_result = conn.execute(self.companies_select)
                for i, company in enumerate(companies_result):
                    company_events = []
                    events_select = EVENTS_SELECT.format(
                        company_id=company['company_id']
                    )
                    try:
                        events_result = conn.execute(events_select)
                        for event in events_result:
                            try:
                                company_events.append(dict(
                                    event_date=event['event_date'],
                                    event_code=event['event_code'],
                                    event_desc=event['event_desc'],
                                    event_url=event['event_url'])
                                )
                            except KeyError:
                                raise
                    except SQLAlchemyError as sq_e:
                        raise
                    try:
                        company_document = dict(
                            company_id=company['company_id'],
                            company_name=company['company_name'],
                            homepage_url=company['homepage_url'],
                            logo_url=company['logo_url'],
                            founded_date=company['founded_date'],
                            country=company['country'],
                            industry=company['industry'],
                            location=company['location'],
                            worker_count=company['worker_count'],
                        )
                    except KeyError:
                        raise
                    yield company_document
        except SQLAlchemyError as sq_e:
            raise

    def push(self, company_document: Dict) -> bool:
        self.insertions += 1
        es_result = self.es_client.index(
            index=self.es_index,
            doc_type='company',
            id=self.insertions,
            body=company_document
        )
        return es_result['created'] and True or False

    def delete_index(self):
        self.es_client.indices.delete(index=self.es_index, ignore=(400, 404))

    def do_import(self):
        self.insertions = 0
        for company_document in self.pull():
            self.push(company_document)
        return self.insertions


