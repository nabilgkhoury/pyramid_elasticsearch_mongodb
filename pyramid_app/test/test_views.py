#!/usr/bin/env python
import unittest

from pyramid import testing
from pyramid.response import Response


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_login(self):
        from pyramid_app.views import login
        request = testing.DummyRequest()

        response = login(request)
        self.assertIn('Login', response['title'])

    def test_search(self):
        from pyramid_app.views import search_companies
        request = testing.DummyRequest()

        response = search_companies(request)
        self.assertIn('Search', response['title'])

    def test_profile(self):
        from pyramid_app.views import company_profile
        request = testing.DummyRequest()

        response = company_profile(request)
        self.assertIn('Profile', response['title'])


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from pyramid_app import main
        app = main()
        from webtest import TestApp

        self.test_app = TestApp(app)

    def test_login(self):
        response = self.test_app.get('/login')
        self.assertEqual('login', response['title'])
        self.assertIn(b'Login', response.body)

    def test_search(self):
        response = self.test_app.get('/search')
        self.assertEqual('search', response['title'])
        self.assertIn(b'Search', response.body)

    def test_profile(self):
        response = self.test_app.get('/company')
        self.assertEqual('company profile', response['title'])
        self.assertIn('bProfile', response.body)
