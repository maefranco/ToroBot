#This program extracts tweets containing certain keywords from the Twitter API

#Import the necessary methods from tweepy library
#from tweepy.streaming import StreamListener
#from tweepy import OAuthHandler
#from tweepy import Stream

import tweepy
import csv

#Variables that contains the user credentials to access Twitter API
#enter variables that can be found in google drive file "twitter-bot notes"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

csvFile = open('tweets.csv', 'a')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, q="#earthquake" and "#southern california", count=1000, lang="en", since_id=2017-11-2).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])


#This is a basic listener that just prints received tweets to stdout.
#class StdOutListener(StreamListener):

   # def on_data(self, data):
       # print (data)
       # return True

   # def on_error(self, status):
       # print (status)


#if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    #l = StdOutListener()
    #auth = OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)
    #stream = Stream(auth, l)

    #This line filters Twitter Streams to capture data by the keywords: 'earthquake', 'southern california'
    #stream.filter(track=['earthquake' and 'southern california'])