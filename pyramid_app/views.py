#!/usr/bin/env python
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='hello')
def hello_world(request):
    print('Request inbound!')
    return Response('Docker works with Pyramid!')


@view_config(route_name='login', renderer='templates/login.jinja2')
def login(request):
    return dict(title='Login Page')


@view_config(route_name='search', renderer='templates/search.jinja2')
def search_companies(request):
    return dict(title='Search Page!')


@view_config(route_name='company', renderer='templates/company.jinja2')
def company_profile(request):
    return dict(title='Company Profile!')

