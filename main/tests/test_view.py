from django.test import TestCase
from ..hashing import Hashing


class TestView(TestCase):
    def setUp(self):
        self.test_link = 'https://test-site.ua/test-page'
        self.hashed_test_link = Hashing.process_url(self.test_link)

    def test_hashed_url_len(self):
        self.assertTrue(0 < len(self.hashed_test_link[1:]) < 21)

    def test_correctness_of_redirection(self):
        response = self.client.get(self.hashed_test_link)
        self.assertEqual(response.url, self.test_link)
