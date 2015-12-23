try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

#GEO_GERMANY = [5.0770049095, 47.2982950435, 15.0403900146, 54.9039819757]
#GEO_ITALY = [5.0770049095, 37.2982950435, 15.0403900146, 44.9039819757]
# User credentials to access Twitter API
keyword = ["flood"]
ACCESS_TOKEN = "591961362-tNmrByTX1pJo8L4DQaSOrS8ZfzliyqcwXME5o6hy"
ACCESS_SECRET = "xBgAMM8xEYCo88G6r7aIv7kEkqniDSw74PX4sfM1YdV2W"
CONSUMER_KEY = "0ftR8LilyGboFvY3gW12Gu1Bz"
CONSUMER_SECRET = "M8v0bLlUpZmvkzszyorSNKBZHGCXg3taBrY44CEryvLZUNjid1"
twitterDataFile = open("twitterFeed.json", "w")

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
for it in keyword:
    iterator = twitter_stream.statuses.filter(track=it)
    #iterator = twitter_stream.statuses.filter(track=keyword, location=[-70.765, 8.160, -71.288, 9.191], place='Brazil')
    #iterator = twitter_stream.statuses.filter(track=keyword, location=[-31.402,114.214,-33.402,116.214])

    #tweet count to be printed
    tweet_count = 100
    for tweet in iterator:
        tweet_count -= 1
        # Twitter Python Tool wraps the data returned by Twitter
        # as a TwitterDictResponse object.
        # Converts it back to the JSON
        print json.dumps(tweet)
        newlinetweet = str(json.dumps(tweet))
        twitterDataFile.write(newlinetweet + '\n')

        # The command below will do pretty printing for JSON data, try it out
        # print json.dumps(tweet, indent=4)

        if tweet_count <= 0:
            break