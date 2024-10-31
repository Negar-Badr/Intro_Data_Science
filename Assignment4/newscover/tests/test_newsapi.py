import unittest
from newscover.newsapi import fetch_latest_news

class TestNewsAPI(unittest.TestCase):

    def setUp(self):
        # Load API key from test_secrets.json
        with open("newscover/tests/test_secrets.json", "r") as file:
            self.api_key = file.read().strip()

    def test_no_keywords(self):
        # Ensure fetch_latest_news fails with no keywords
        result = fetch_latest_news(self.api_key, [])
        self.assertEqual(len(result), 0)

    def test_lookback_days(self):
        # Test lookback_days parameter
        result = fetch_latest_news(self.api_key, ["election"], lookback_days=1)
        # Ensure that articles are within the specified timeframe
        self.assertTrue(all(article['publishedAt'] >= (datetime.now() - timedelta(days=1)).isoformat() for article in result))

    def test_invalid_keywords(self):
        # Ensure function fails when non-alphabetic characters are provided
        with self.assertRaises(ValueError):
            fetch_latest_news(self.api_key, ["123news"])
