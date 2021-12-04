from flask import Flask, request, render_template
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import nltk
import re
nltk.download('stopwords')

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    stop_words = stopwords.words('english')
    text = request.form['text'].lower()
    text_no_processing = request.form['text'].lower()
    text = re.sub(r'[^\w\s]','',text)
    text = ' '.join([x for x in text.split() if x not in stop_words])
    obj = SentimentIntensityAnalyzer()
    sentiment= obj.polarity_scores(text)
    neg = sentiment['neg']*100
    neu = sentiment['neu']*100
    pos = sentiment['pos']*100
    compound = sentiment['compound']
    if compound >= 0.05:
        return render_template('index.html', final=pos,finalP=pos,finalNeu=neu,finalNeg=neg, text=text, text_no_processing=text_no_processing, compound=compound)
    elif compound <= -0.05:
        return render_template('index.html', final=neg,finalP=pos,finalNeu=neu,finalNeg=neg, text=text, text_no_processing=text_no_processing, compound=compound)
    else:
        return render_template('index.html', final=neu,finalP=pos,finalNeu=neu,finalNeg=neg, text=text, text_no_processing=text_no_processing, compound=compound)

