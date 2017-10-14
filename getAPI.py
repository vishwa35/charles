import tweepy
from charles import keys

def getAPI():
	auth = tweepy.OAuthHandler(keys['consumerKey'], keys['consumerSecret'])
	auth.set_access_token(key['accessToken'], keys['accessSecret'])
	api = tweepy.API(auth)
	return api