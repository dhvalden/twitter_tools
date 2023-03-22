import configparser
import tweepy
import json


def main():
    config = configparser.RawConfigParser()
    config.read('./get_timeline.config')

    access_token = config['KEYS']['Access_Token']
    access_token_secret = config['KEYS']['Access_Token_Secret']
    consumer_key = config['KEYS']['Api_Key']
    consumer_secret = config['KEYS']['Api_Secret_Key']
    bearer_token = config['KEYS']['Bearer_Token']

    client = tweepy.Client(bearer_token=bearer_token,
                           consumer_key=consumer_key,
                           consumer_secret=consumer_secret,
                           access_token=access_token,
                           access_token_secret=access_token_secret)

    id = '365106165'

    for tweet in tweepy.Paginator(client.get_users_tweets,
                                  id=id,
                                  tweet_fields=['public_metrics',
                                                'created_at'],
                                  max_results=100).flatten(limit=10000):
        print(json.dumps(tweet.data))


if __name__ == '__main__':
    main()
