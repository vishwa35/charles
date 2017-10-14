from flask import Flask
from sentiment import Sentiment
import json

app = Flask(__name__)

@app.route("/")
def hello():
    s = Sentiment("Trump")
    return json.dumps(s.get_tweets())

if __name__ == "__main__":
    app.run()
