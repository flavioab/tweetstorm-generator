from unittest import TestCase
from tweetstorm_generator.core import get_tweets


class TestCore(TestCase):

    def test_get_tweets(self):
        text = '1' * 180
        tweets = get_tweets(text=text, color=False)
        expected = [
            '1/2 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
            '2/2 11111111111111111111111111111111111111111111'
        ]
        self.assertEquals(expected, tweets)

        for tweet in tweets:
            self.assertTrue(len(tweet) <= 140)
