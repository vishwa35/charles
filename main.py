from flask import Flask, render_template
from sentiment import Sentiment
import json

app = Flask(__name__)

@app.route("/")
def hello():
    s = Sentiment("Trump")
    return render_template('index.html')
    # return json.dumps(s.get_tweets())

if __name__ == "__main__":
    app.run()
