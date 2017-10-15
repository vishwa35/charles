from sentiment import TSentiment
import datetime
from datetime import timedelta


s = TSentiment("Hurricane")
numOfTweets = 250
tweetMap = {}
daysAgo = 10

while daysAgo >= 0:
    since = (datetime.datetime.now() - timedelta(days=daysAgo)).strftime("%Y-%m-%d")
    until = (datetime.datetime.now() - timedelta(days=daysAgo-1)).strftime("%Y-%m-%d")
    tweets = s.get_tweets(numOfTweets, since, until)

    tweetsObtained = len(tweets)
    positiveTweets = 0
    negativeTweets = 0
    neutralTweets = 0
    for tweet in tweets:
        if tweet[2] == 'positive':
            positiveTweets += 1
        elif tweet[2] == 'negative':
            negativeTweets += 1
        else:
            neutralTweets += 1
        
    positivePercentage = round(positiveTweets/float(tweetsObtained), 2)
    negativePercentage = round(negativeTweets/float(tweetsObtained), 2)
    neutralPercentage = round(neutralTweets/float(tweetsObtained), 2)
    tweetMap[since] = (positivePercentage, negativePercentage, neutralPercentage)

    # for tweet in tweets:
    #     print tweet[0].encode('ascii', 'replace') + '\n' + tweet[1] + '\n' + tweet[2]
    #     print '----------------------------------------------------------------------'
    daysAgo -= 1

for time in tweetMap:
    print time + " " + str(tweetMap[time][0]) + " percent positive, " + str(tweetMap[time][1]) + " percent negative, " + str(tweetMap[time][2]) + " percent neutral"



# tweets = s.get_tweets(10, "2017-10-14", "2017-10-15")

# for tweet in tweets:
#     print tweet[0].encode('ascii', 'replace') + '\n' + tweet[1] + '\n' + tweet[2]
#     print '----------------------------------------------------------------------'
# now = datetime.datetime.now()
# past = datetime.datetime.now() - timedelta(days=10)
# print past.strftime("%Y-%m-%d")
