from flask import Flask, render_template, g, request
from sentiment import Sentiment
import json
import sqlite3

app = Flask(__name__)
DATABASE = 'charles.db'

def connect():
    with app.app_context():
        return get_db()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection():
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = connect().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/sent_json")
def tweet_sent():
    s = Sentiment("Trump")
    return json.dumps(s.get_tweets())

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    return text
    # s = Sentiment(text)
    # return json.dumps(s.get_tweets())
    # processed_text = text.upper()
    # return processed_text

if __name__ == "__main__":
    for user in query_db('select * from users'):
        print user['name']
    app.run()
    close_connection()
