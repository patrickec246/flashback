**tweet_rate_hrs** : number of hours between posts

**realtime** : whether sampled tweets should be strictly chronological. Otherwise, tweets may be sampled out of order in 24-hour increments.

**account** : an account to source tweets from
 - **user** - twitter username
 - **sample_mode** - how to choose which tweets to retweet
	 - **popular** - sample high traffic tweets
	 - **random** - randomly sample
	 - **weight** - weight (cumulative), used for *weighted_heap* selection algorithm

**selection_algorithm** : algorithm for selecting the next account to sample a tweet from

 - **random** - randomly sample an account from listed accounts
 - **weighted_heap** - selects accounts based on their weights
