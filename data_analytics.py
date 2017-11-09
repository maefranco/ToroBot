# This program analyzes the data found in twitter_data.txt

import json
import pandas as pd
import matplotlib.pyplot as plt
import re

tweets_data_path = 'twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

#print (len(tweets_data))

# add text and language columns to tweets DataFrame
tweets = pd.DataFrame()
tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data))
print (len(tweets['lang']))

# create chart of top 5 countries from where tweets were sent
tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=10)
ax.set_ylabel('Number of Tweets', fontsize=10)
ax.set_title('Top 5 Languages Used in Tweets', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=10)
ax.set_ylabel('Number of Tweets' , fontsize=15)
ax.set_title('Top 5 Countries of Tweet Origin', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='green')

plt.show()

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets['earthquake'] = tweets['text'].apply(lambda tweet: word_in_text('earthquake', tweet))
tweets['southern california'] = tweets['text'].apply(lambda tweet: word_in_text('southern california', tweet))

print (tweets['earthquake'].value_counts()[True])
print (tweets['southern california'].value_counts()[True])

words = ['earthquake', 'southern california']
tweets_by_words =[tweets['earthquake'].value_counts()[True], tweets['southern california'].value_counts()[True]]

x_pos = list(range(len(words)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_words, width, alpha=1, color='b')
ax.set_ylabel('Number of Tweets', fontsize=10)
ax.set_title('Number of Tweets Containing Each Keyword', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(words)
plt.show()


