#!/usr/bin/env python
from pyramid.config import Configurator


def main():
    config = Configurator()
    config.include('pyramid_jinja2')

    # add routes
    config.add_route('hello', '/')
    config.add_route('login', '/login')
    config.add_route('search', '/search')
    config.add_route('company', '/company')

    # scan views
    config.scan('.views')

    return config.make_wsgi_app()
