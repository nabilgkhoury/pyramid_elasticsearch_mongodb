#!/usr/bin/env python

import unittest
from pyramid_app.utils.sql_es_import import SQLToESImporter


class TestSQLToESImporter(unittest.TestCase):
    def setUp(self):
        self.sql_to_es_importer = SQLToESImporter(
            company_count=1, es_index='test'
        )
        self.sql_to_es_importer.delete_index()
        self.documents = self.sql_to_es_importer.pull()

    def tearDown(self):
        self.sql_to_es_importer.delete_index()

    def test_sql_pull(self):
        self.assertTrue(len(list(self.documents)) == 1)

    def test_es_push(self):
        inserted = 0
        for document in self.documents:
            inserted = self.sql_to_es_importer.push(document)
        self.assertTrue(inserted)


if __name__ == '__main__':
    unittest.main()
