import unittest

from pyramid_app.es_search import ESSearch


class TestESSearch(unittest.TestCase):
    es_search: ESSearch

    def setUp(self):
        self.es_search = ESSearch()

    def test_search_by_name(self):
        hits = self.es_search.search_by_name('microsoft')
        self.assertEqual(len(hits), 1)

    def test_search_by_location(self):
        hits = self.es_search.search_by_location('seattle')
        self.assertEqual(len(hits), 1)

    def test_search_by_event(self):
        hits = self.es_search.search_by_event('democratic')
        self.assertEqual(len(hits), 1)

    def test_search_by_text(self):
        hits = self.es_search.search_by_text('wild stuff')
        self.assertEqual(len(hits), 1)


if __name__ == '__main__':
    unittest.main()
