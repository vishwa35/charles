import re, praw, sys
from textblob import TextBlob
import keys

class RSentiment(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        user = keys.keys['redditUser']
        password = keys.keys['redditPassword']
        clientID = keys.keys['redditID']
        secret = keys.keys['redditSecret']

        # attempt authentication
        self.reddit = praw.Reddit(client_id = clientID, client_secret = secret, password = password, username = user, user_agent = 'charles bot')
        print self.reddit.user.me()

    def sanitize(self, text):
        '''
        Utility function to clean text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

    def get_sentiment(self, text):
        # create TextBlob object of passed text
        analysis = TextBlob(self.sanitize(text))
        return analysis.sentiment.polarity
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_comments(self,sub, keyword):
        '''
        Main function to fetch comments and parse them.
        '''
        results = list(self.reddit.subreddit(sub).search(keyword))
        ans = []
        val = 0
        print(len(results))
        for submission in results:
            ans.append(submission.title)
            val += self.get_sentiment(submission.title) / len(results)
        return val

stuff = RSentiment()
print stuff.get_comments(sys.argv[1], sys.argv[2])