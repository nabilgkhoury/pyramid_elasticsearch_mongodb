#!/usr/bin/env python

from elasticsearch2 import Elasticsearch

from pyramid_app import ES_INDEX, ES_CONNECT


class ESSearch(object):
    es_client: Elasticsearch
    es_index: str

    def __init__(self, connect=ES_CONNECT, index=ES_INDEX):
        self.es_client = Elasticsearch(connect)
        self.es_index = index

    def search_by_name(self, search: str):
        res = self.es_client.search(
            index=self.es_index,
            doc_type='company',
            body=dict(
                query=dict(
                    match_phrase=dict(
                        company_name=search
                    )
                )
            )
        )
        return [company['_source'] for company in res['hits']['hits']]

    def search_by_location(self, search: str):
        res = self.es_client.search(
            index=self.es_index,
            doc_type='company',
            body=dict(
                query=dict(
                    match_phrase=dict(
                        location=search
                    )
                )
            )
        )
        return [company['_source'] for company in res['hits']['hits']]

    def search_by_id(self, company_id: str):
        res = self.es_client.search(
            index=self.es_index,
            doc_type='company',
            body=dict(
                query=dict(
                    match=dict(
                        company_id=company_id
                    )
                )
            )
        )
        if len(res['hits']['hits']):
            return res['hits']['hits'][0]['_source']
        else:
            return {}

    def search_by_text(self, text: str):
        res = self.es_client.search(
            index=self.es_index,
            doc_type='company',
            body=dict(
                query=dict(
                    query_string=dict(
                        query=text
                    )
                )
            )
        )
        return [company['_source'] for company in res['hits']['hits']]

