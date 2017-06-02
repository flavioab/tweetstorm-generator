from .core import get_tweets
from .console import get_text


def main():
    text = get_text()
    if text:
        for tweet in get_tweets(text):
            print(tweet)
