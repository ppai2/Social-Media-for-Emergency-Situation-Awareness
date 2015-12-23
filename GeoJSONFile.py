import json

# Tweets are stored in "fname"
with open("twitterFeed.json", 'r') as f:
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        tweet = json.loads(line)
        if tweet['coordinates']:
            geo_json_feature = {
                "type": "Feature",
                "geometry": tweet['coordinates'],
                "properties": {
                    "text": tweet['text'],
                    "created_at": tweet['created_at']
                }
            }
            geo_data['features'].append(geo_json_feature)

# Save geo data
print "Data printed in the geo_data file"
with open('geo_data.json', 'w') as fout:
    fout.write(json.dumps(geo_data, indent=4))