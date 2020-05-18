#!/usr/bin/env python
import unittest

from pyramid import testing
from pyramid_app.views import (
    login,
    search_companies,
    company_profile
)


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_login(self):
        request = testing.DummyRequest()
        response = login(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.body)

    def test_search(self):
        request = testing.DummyRequest()
        response = search_companies(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Search', response.body)

    def test_profile(self):
        request = testing.DummyRequest()
        response = company_profile(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Profile', response.body)
