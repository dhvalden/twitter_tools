import configparser
import tweepy
import pandas as pd


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
                           access_token_secret=access_token_secret,
                           wait_on_rate_limit=True)

    id = '365106165'

    users = []

    for user in tweepy.Paginator(client.get_users_followers,
                                 id=id,
                                 max_results=100).flatten(limit=10000):
        users.append(user.data['username'])

    data = pd.DataFrame({'followers': users})
    data.to_csv('followers_2.csv')


if __name__ == '__main__':
    main()
