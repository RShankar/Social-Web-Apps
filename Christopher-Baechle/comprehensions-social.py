import twitter
import json
import numpy as np
import pandas as pd
import re

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

#Get my home timeline as json structure
my_timeline = twitter_api.statuses.home_timeline()
fmt_timeline = json.dumps(my_timeline, indent=4, separators=(',', ': '))

#dump to file
with open("my-timeline.txt", "w") as out:
    out.write(fmt_timeline)

#Just get the text for the tweets
[entry['text'] for entry in my_timeline]

#Text too long, truncate at 50 chars
[entry['text'][0:50] for entry in my_timeline]

#Get all the users that tweeted in timeline
[ entry['user']['screen_name'] for entry in my_timeline ]

#Make a dictionary of user to tweets
{ entry['user']['screen_name']:entry['text'][0:50] for entry in my_timeline }

#Update your status from python
#t.statuses.update(status="First status update from code")

results = twitter_api.search.tweets(q="#pycon")

#Show writing a function
def write_pretty_json(filename,data):
    fmt_data = json.dumps(data, indent=4, separators=(',', ': '))
    with open(filename, "w") as out:
        out.write(fmt_data)

#Use our function
write_pretty_json('pycon-search.txt', results)

#Get all the hashtags for results as 2-dimensions
[ hashtags['text'] for entry in results['statuses'] for hashtags in entry['entities']['hashtags'] ]

#Discuss what the u'mytext' is (aka it's unicode)

#
#Pandas portion
#
#Get tweets into csv like format

#Turn into 2d matrix
[ [entry['user']['screen_name'],entry['created_at'],entry['geo'],entry['place'],entry['text'],entry['retweeted']] for entry in results['statuses'] ]

#Turn into 2d matrix
results_matrix = [ [entry['user']['screen_name'],entry['created_at'],entry['geo'],entry['place'],entry['text'],entry['retweeted']] for entry in results['statuses'] ]

#Turn into DataFrame
df = pd.DataFrame(results_matrix)

#Turn into DataFrame with column names
df = pd.DataFrame(results_matrix,columns=['ScreenName','CreatedAt','Geo','Place','Text','Retweeted'])

#Get all the unique screen names returned
df['ScreenName'].unique()

#Find the number of unique screen names returned
df['ScreenName'].unique().size

#Write results to csv
df.to_csv('results.csv', sep=',', encoding='utf-8')



