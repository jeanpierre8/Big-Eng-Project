import time
import redis
from flask import Flask, render_template
from flask import request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    return render_template('index.html')
"""

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/',methods=['GET'])
def Sentence_print():
    sentence = request.args.get('Sentence')
    sentence = sentence.strip('-"][').replace('-',' ').split('.')
    return "Your sentence is : {}".format(sentence)

    obj = SentimentIntensityAnalyzer()
    sentiment=obj.polarity_scores(sentence)

    return ("sentence was rated as ", sentiment['neg']*100, "% Negative")

    print("sentence was rated as ", sentiment['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment['pos']*100, "% Positive")
    print("")
    if sentiment['compound']>=0.05:
        print("The sentiment is Positive")
    elif sentiment['compound']<= 0.05:
        print("The sentiment is Negative")
    else:
        print("The sentiment is Neutral")
"""


