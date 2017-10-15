import re, praw
from textblob import TextBlob
import keys

class RSentiment(object):
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

            self.reddit = praw.Reddit(client_id='my client id',
                 client_secret='my client secret',
                 user_agent='my user agent')

        except:
            print("Error: Authentication Failed")

    def sanitize(self, text):
        '''
        Utility function to clean text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

    def get_sentiment(self, text):
        # create TextBlob object of passed text
        analysis = TextBlob(self.sanitize(text))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_comments(self, count = 10):
        '''
        Main function to fetch comments and parse them.
        '''

        try:
            # fetch 10 hot submissions
            submissions = reddit.subreddit(keyword).hot(limit=10)
            comments = []
            parsed_reddit = []
            for sub in submissions:
                # sub.created would definitely work, not sure abou comment.created
                comments += list(sub.comments)

            # parsing comments one by one
            for comment in comments:
                # empty dictionary to store required params of a comment
                parsed = (comment.created.strftime("%m/%d/%Y"), self.get_sentiment(comment.parse))
                parsed_reddit.append(parsed)

            return parsed_reddit

    except Error as e:
            # print error (if any)
            print("Error : " + str(e))
