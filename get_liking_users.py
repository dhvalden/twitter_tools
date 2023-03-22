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
    ids_list = pd.read_csv('ids.csv')['id'].to_list()

    client = tweepy.Client(bearer_token=bearer_token,
                           consumer_key=consumer_key,
                           consumer_secret=consumer_secret,
                           access_token=access_token,
                           access_token_secret=access_token_secret,
                           wait_on_rate_limit=True
                           )

    my_user = []
    for id in ids_list:
        users = client.get_liking_users(id=id)
        try:
            for user in users.data:
                my_user.append(user)
        except TypeError:
            continue

    data = pd.DataFrame({'liking_user': my_user})
    data.to_csv('liking_user.csv')


if __name__ == '__main__':
    main()
