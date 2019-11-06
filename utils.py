import json
import tweepy
import errno
import random

import asyncio

from os import path

def load_config(filepath):
    if not path.exists(filepath):
        return None

    with open(filepath) as f:
        json_obj = json.loads(f.read())
        return json_obj

class FlashbackClient(object):
    def __init__(self, config):
        self.config = config
        self.users = None

        err = self.authenticate()
        if err == 1000: #TODO we're almost there, fix once we get API
            raise Exception('Unable to authenticate twitter account, err {}'.format(err))

    def authenticate(self):
        if self.config is None:
            return errno.EINVAL

        self.auth = tweepy.OAuthHandler(
                self.config['auth']['CONSUMER_KEY'],
                self.config['auth']['CONSUMER_SECRET']
                )

        self.auth.set_access_token(
                self.config['auth']['ACCESS_TOKEN'],
                self.config['auth']['ACCESS_TOKEN_SECRET']
                )

        try:
            self.auth.verify_credentials()
            self.api = tweepy.API(auth)
        except:
            return errno.EACCES

        return 0

    def tweet(self, tweet):
        return api.update_status(tweet)

    def sample_tweet(self):
        user = self.sample_user()

        tweets = self.api.search(
            result_type='mixed',
            lang='en',
            count=10,
            until=self.last_date,
            q='(from%3{})'.format(user['user'])
            )

        return tweets[0] #TODO fix

    def sample_user(self):
        if self.users is None:
            self.users = list(self.config['accounts'])

        if self.config['selection_algorithm'] == 'random':
            return random.choice(self.users)
        elif self.config['selection_algorithm'] == 'weighted_heap':
            return random.choices(
                    population=self.users,
                    weights=[user['weight'] for user in self.users],
                    k=1)
        else:
            return None

    def main(self):
        while True:
            #self.tweet(self.sample_tweet())
            asyncio.run(asyncio.sleep(int(self.config['post_rate_hrs']) * 60 * 60))
            print('ye')
