import textblob

class Analysis:
    self.map = {}
    
    def get_sentiment(self, tweet):
        tweet = tweet
        analysis = TextBlob(tweet)
        map.add(tweet.time, analysis.sentiment.polarity)
        return analysis.sentiment.polarity


for
