from flask import Flask, render_template, g, request
from sentiment import TSentiment
from reddit import RSentiment
import datetime
from datetime import timedelta
# from reddit import RSentiment

import json
import sqlite3

app = Flask(__name__)
# DATABASE = 'charles.db'

# def connect():
#     with app.app_context():
#         return get_db()
#
# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db
#
# @app.teardown_appcontext
# def close_connection():
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()
#
# def query_db(query, args=(), one=False):
#     cur = connect().execute(query, args)
#     rv = cur.fetchall()
#     cur.close()
#     return (rv[0] if rv else None) if one else rv

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/sent_json")
def tweet_sent(text):
    s = TSentiment(text)
    return json.dumps(s.get_tweets())

@app.route('/req', methods=['GET'])
def my_form_get():
    text =  request.args.get('text')
    # print(text + ":")
    # print tweet_sent(text)
    tweetscrape(text)
    redditscrape(text)
    return render_template('volume_distribution_vis.html')

@app.route('/back', methods=['GET'])
def my_form_back():
    # text = request.args.get('text')
    # print(text)
    return render_template('index.html')
#
# @app.route('/show', methods=['GET'])
# def my_form_show():
#     # text = request.args.get('text')
#     # print(text)
#     return render_template('index.html')

def tweetscrape(topic):
    s = TSentiment(topic)
    numOfTweets = 10
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
        # positivePercentage = round(positiveTweets/float(tweetsObtained), 2)
        # negativePercentage = round(negativeTweets/float(tweetsObtained), 2)
        # neutralPercentage = round(neutralTweets/float(tweetsObtained), 2)

        # print "Volume for " + since + ": " + str(tweetsObtained)

        # Store each day's unique values in our tweet map
        tweetMap[since] = str(positiveTweets) + ', ' + str(neutralTweets) + ', ' + str(negativeTweets) + ', ' + '0'

        # for tweet in tweets:
        #     print tweet[0].encode('ascii', 'replace') + '\n' + tweet[1] + '\n' + tweet[2]
        #     print '----------------------------------------------------------------------'
        daysAgo -= 1

    write_csvfile = "./static/sentiment_data.csv"
    csv = open(write_csvfile, "w")
    csv.write('Sentiment,Positive,Neutral,Negative,' + topic + '\n')
    for timeStamp in tweetMap:
        csv.write(timeStamp + ', ' + tweetMap[timeStamp] + '\n')

    # for time in tweetMap:
    #     print time + " " + str(tweetMap[time][0]) + " percent positive, " + str(tweetMap[time][1]) + " percent negative, " + str(tweetMap[time][2]) + " percent neutral"


def redditscrape(keyword, sub='all'):
    s = RSentiment()


    # Count from 10 days ago to include every single day time interval
    positive = 0
    neutral = 0
    negative = 0
    reddit = s.get_comments(sub, keyword)
    for comment in reddit:
    	if comment > 0:
    		positive += 1
    	if comment == 0:
    		neutral += 1
    	else:
    		negative += 1

    write_csvfile = "./static/reddit_data.csv"
    csv = open(write_csvfile, "w")
    csv.write('Sentiment,Content,' + sub + " : " + keyword + '\n')
    csv.write("Negative" + ', ' + str(negative) + ',0\n')
    csv.write("Neutral" + ', ' + str(neutral) + ',0\n')
    csv.write("Positive" + ', ' + str(positive) + ',0\n')

if __name__ == "__main__":
    # for user in query_db('select * from users'):
    #     print user['name']
    app.run()
