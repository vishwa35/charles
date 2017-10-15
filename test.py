from sentiment import TSentiment
import datetime
from datetime import timedelta

# s = TSentiment("Trump")
# tweets = s.get_tweets()

# for tweet in tweets:
#     print tweet[0].encode('ascii', 'replace') + '\n' + tweet[1] + '\n' + tweet[2]
#     print '----------------------------------------------------------------------'
now = datetime.datetime.now()
past = datetime.datetime.now() - timedelta(days=9)
print past.strftime("%Y-%m-%d")
