#!/usr/bin/env python
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound

from pyramid_app.es_search import ESSearch


@view_config(route_name='hello')
def hello_world(request):
    return HTTPFound(location='/search')


@view_config(route_name='login', renderer='templates/login.jinja2')
def login(request):
    return dict(title='Login Page')


@view_config(route_name='search', renderer='templates/search.jinja2')
def search_companies(request):
    text = request.params.get('search_field', '')
    hits = []
    if text:
        es_search = ESSearch()
        hits = es_search.search_by_text(text=text)
    return dict(title='Search Page', text=text, hits=hits)


@view_config(route_name='company', renderer='templates/company.jinja2')
def company_profile(request):
    company_id = request.params.get('company_id', '')
    if company_id:
        es_search = ESSearch()
        company_doc = es_search.search_by_id(company_id=company_id)
        return dict(title='Company Profile', company=company_doc)
    else:
        raise HTTPNotFound()

