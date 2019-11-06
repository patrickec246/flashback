import tweepy
import argparse

from utils import *

CONFIG_FILE = "config.json"

def main():
    config = load_config(CONFIG_FILE)

    client = FlashbackClient(config)

    client.main()

if __name__=='__main__':
    main()
