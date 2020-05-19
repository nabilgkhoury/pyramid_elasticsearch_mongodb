#!/usr/bin/env python

from elasticsearch2 import Elasticsearch

from pyramid_app import ES_INDEX, ES_CONNECT


class ESSearch(object):
    es_client: Elasticsearch

    def __init__(self, connect=ES_CONNECT):
        self.es_client = Elasticsearch(ES_CONNECT)

    def search_by_name(self, search: str):
        raise NotImplementedError

    def search_by_location(self, search: str):
        raise NotImplementedError

    def search_by_event(self, search: str):
        raise NotImplementedError

    def search_by_text(self, text: str):
        raise NotImplementedError

