#!/usr/bin/env python

import unittest
from pyramid_app.utils.sql_es_import import SQLToESImporter


class TestSQLToESImporter(unittest.TestCase):
    def setUp(self):
        self.sql_to_es_importer = SQLToESImporter(
            company_count=5, es_index='test'
        )

    def tearDown(self):
        self.sql_to_es_importer.delete_index()

    def test_sql_pull(self):
        documents = list(self.sql_to_es_importer.pull())
        self.assertEqual(len(documents), 5)

    def test_es_push(self):
        inserted = 0
        for document in self.sql_to_es_importer.pull():
            if self.sql_to_es_importer.push(document):
                inserted += 1
        self.assertEqual(inserted, 5)

    def test_es_reimport(self):
        insertions = self.sql_to_es_importer.reimport()
        self.assertEqual(insertions, 5)


if __name__ == '__main__':
    unittest.main()
