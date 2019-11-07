import tweepy
import argparse

from utils import *

CONFIG_FILE = "config.json"

def main():
    client = FlashbackClient(config=CONFIG_FILE)

    client.main()

if __name__=='__main__':
    main()
