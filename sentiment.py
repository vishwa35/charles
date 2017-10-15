import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import keys

class TSentiment(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self, keyword):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = keys.keys['consumerKey']
        consumer_secret = keys.keys['consumerSecret']
        access_token = keys.keys['accessToken']
        access_token_secret = keys.keys['accessSecret']

        self.topic = keyword
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0.33:
            return 'positive'
    elif analysis.sentiment.polarity < -0.33:
            return 'negative'
        else:
            return 'neutral'

    def get_tweets(self, count, sinceTime, untilTime):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = self.topic, count = count, since = sinceTime, until = untilTime)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = (tweet.text, tweet.created_at.strftime("%m/%d/%Y"), self.get_tweet_sentiment(tweet.text))

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
