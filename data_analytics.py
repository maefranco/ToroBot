# This program analyzes the data found in twitter_data.txt

import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = '.../ToroBot/twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print (len(tweets_data))

#tweets = pd.DataFrame()

