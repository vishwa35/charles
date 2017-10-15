from sentiment import TSentiment
import datetime
from datetime import timedelta


s = TSentiment("Irma")
numOfTweets = 250
tweetMap = {}
daysAgo = 10

# Count from 10 days ago to include every single day time interval
while daysAgo >= 0:
    since = (datetime.datetime.now() - timedelta(days=daysAgo)).strftime("%Y-%m-%d")
    until = (datetime.datetime.now() - timedelta(days=daysAgo-1)).strftime("%Y-%m-%d")
    tweets = s.get_tweets(numOfTweets, since, until)

    # Tally up positive, negative, and neutral sentiment among the tweets per day
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
    
    # Calculate the percentage distribution
    positivePercentage = round(positiveTweets/float(tweetsObtained), 2)
    negativePercentage = round(negativeTweets/float(tweetsObtained), 2)
    neutralPercentage = round(neutralTweets/float(tweetsObtained), 2)

    # Store each day's unique values in our tweet map
    tweetMap[since] = (positivePercentage, negativePercentage, neutralPercentage)

    # for tweet in tweets:
    #     print tweet[0].encode('ascii', 'replace') + '\n' + tweet[1] + '\n' + tweet[2]
    #     print '----------------------------------------------------------------------'
    daysAgo -= 1

for time in tweetMap:
    print time + " " + str(tweetMap[time][0]) + " percent positive, " + str(tweetMap[time][1]) + " percent negative, " + str(tweetMap[time][2]) + " percent neutral"

