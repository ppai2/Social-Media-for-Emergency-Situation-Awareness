# Import the necessary package to process data in JSON format

import json

# We use the file saved from last step as example
tweets_filename = 'twitterFeed.json'
tweets_file = open(tweets_filename, "r")

for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object
        decoded = json.loads(line)
        if 'text' in decoded:  # only messages contains 'text'field is a tweet
            #print "Tweet JSON: ", decoded
            print "Tweet text: ", decoded['text']
            print "Tweet user ID: ", decoded['user']['id']

            print "Static location of the user: ", decoded['user']['location']
            print "User screen name: ", decoded['user']['name']
            print "Tweet creation date: ", decoded['user']['created_at']
            print"************************************************************"
            geo_coordinates = []
            for hashtag in decoded['geo']['coordinates']:
                geo_coordinates.append(decoded['geo']['coordinates'])
            print "Tweet user location: ", geo_coordinates
            print"****************This tweet contains location********************************************"
            print"************************************************************"
    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue