#This program extracts tweets containing certain keywords from the Twitter API

#Import the necessary methods from tweepy library
#from tweepy.streaming import StreamListener
#from tweepy import OAuthHandler
#from tweepy import Stream

import tweepy
import csv

#Variables that contains the user credentials to access Twitter API
access_token = "926157826342371329-z1HRWsNes6zSLvzMyUmvy3nB4Kg2qOd"
access_token_secret = "2041mVPf7a4qU3aNKkWJmOYd1MaSr6EP7mu81TBLMPUbF"
consumer_key = "4oRhSMKUB3d5Sd364CjrIQSOd"
consumer_secret = "sULa9DU1dD7Npym4DDQKLuILsmfPXQvfMjG8Qti5sN4pNzFtgr"
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