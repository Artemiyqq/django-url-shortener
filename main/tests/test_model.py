from django.test import TestCase
from ..hashing import Hashing


class ModelTest(TestCase):
    def setUp(self):
        self.test_link = 'https://test-site.ua/test-page'
        self.hashed_test_link = Hashing.process_url(self.test_link)

    def test_returns_hashed_link(self):
        received_hashed_url = Hashing.get_hashed_url(self.test_link)
        self.assertEqual(received_hashed_url, self.hashed_test_link)

    def test_returns_original_link(self):
        received_original_url = Hashing.get_original_url(self.hashed_test_link)
        self.assertEqual(received_original_url, self.test_link)
