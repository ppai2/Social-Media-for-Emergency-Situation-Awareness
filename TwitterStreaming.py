#Import the necessary methods from tweepy library
from sys import stderr

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, API
from tweepy import Stream
import json

keyword = 'earthquake'
GEO_GERMANY = [5.0770049095, 47.2982950435, 15.0403900146, 54.9039819757]
GEO_ITALY = [5.0770049095, 37.2982950435, 15.0403900146, 44.9039819757]

#Variables that contains the user credentials to access Twitter API
access_token = "591961362-tNmrByTX1pJo8L4DQaSOrS8ZfzliyqcwXME5o6hy"
access_token_secret = "xBgAMM8xEYCo88G6r7aIv7kEkqniDSw74PX4sfM1YdV2W"
consumer_key = "0ftR8LilyGboFvY3gW12Gu1Bz"
consumer_secret = "M8v0bLlUpZmvkzszyorSNKBZHGCXg3taBrY44CEryvLZUNjid1"

"""
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

    def on_exception(self, exception):
        print exception


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'AfghanistanEarthquake'
    stream.filter(track=[keyword], locations=[-20.65, 38.71, -20.66, 38.72], encoding="UTF-8")
"""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

iterator = ""
tweet_count = 0

twitterDataFile = open("twitterFeed.json", "w")

class CustomStreamListener(StreamListener):
    """def on_data(self, data):
        print data
        return True
    """

    def on_status(self, status):
        if keyword:
            """print "Text in the tweet :", status.text
            #print "User object :", status.author
            print "User ID :", status.author.id
            print "User author location :", status.author.location
            #print "Tweet creation date :", status.author.created_at
            print status
            #print "Place object :", status.place
            print "\n"
            """
            for tweet in iterator:
                tweet_count -= 1
                print json.dumps(tweet)
                newlinetweet = str(json.dumps(tweet))
                twitterDataFile.write(newlinetweet + '\n')



    def on_error(self, status_code):
        print >> stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = Stream(auth, CustomStreamListener())
iterator = sapi.filter(track=[keyword])

tweet_count = 10
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet)
    newlinetweet = str(json.dumps(tweet))
    twitterDataFile.write(newlinetweet + '\n')

    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)

    if tweet_count <= 0:
        break
