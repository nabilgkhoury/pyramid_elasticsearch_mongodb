#!/usr/bin/env python
from pyramid.config import Configurator

# es connection
ES_CONNECT = (dict(host='es-service', port=9200),)
ES_INDEX = 'crunshbase'


def main():
    config = Configurator()
    config.include('pyramid_jinja2')

    # add routes
    config.add_route('hello', '/')
    config.add_route('login', '/login')
    config.add_route('search', '/search')
    config.add_route('company', '/company')
    config.add_static_view(name='static', path='pyramid_app:static')

    # scan views
    config.scan('.views')

    return config.make_wsgi_app()
