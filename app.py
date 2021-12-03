from flask import Flask, request, render_template
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text'].lower()
    obj = SentimentIntensityAnalyzer()
    sentiment= obj.polarity_scores(text)
    neg = sentiment['neg']*100
    neu = sentiment['neu']*100
    pos = sentiment['pos']*100
    compound = sentiment['compound']
    if compound >= 0.05:
        return render_template('index.html', final=pos,finalP=neg,finalNeu=neu,finalNeg=neg, text=text)
    elif compound <= 0.05:
        return render_template('index.html', final=neg,finalP=neg,finalNeu=neu,finalNeg=neg, text=text)
    else:
        return render_template('index.html', final=neu,finalP=neg,finalNeu=neu,finalNeg=neg, text=text)

"""
import redis
from flask import Flask, render_template
from flask import request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    return render_template('index.html')
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
