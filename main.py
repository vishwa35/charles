from flask import Flask
from sentiment import Sentiment

app = Flask(__name__)

@app.route("/")
def hello():
    s = Sentiment("Trump")
    # return s.get_tweets()[0]['sentiment']
    return "Hello World!"

if __name__ == "__main__":
    app.run()
