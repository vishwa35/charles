from sentiment import TSentiment
import datetime
from datetime import timedelta

s = TSentiment("Trump")
tweets = s.get_tweets(10, "2017-10-04", "2017-10-06")

for tweet in tweets:
    print tweet[0].encode('ascii', 'replace') + '\n' + tweet[1] + '\n' + tweet[2]
    print '----------------------------------------------------------------------'
# now = datetime.datetime.now()
# past = datetime.datetime.now() - timedelta(days=10)
# print past.strftime("%Y-%m-%d")
