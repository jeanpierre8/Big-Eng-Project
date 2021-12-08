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
    neg = "{:.2f}".format(neg)
    neu = sentiment['neu']*100
    neu = "{:.2f}".format(neu)
    pos = sentiment['pos']*100
    pos = "{:.2f}".format(pos)
    compound = sentiment['compound']
    if compound >= 0.05:
        return render_template('index.html', final=pos,finalP=pos,finalNeu=neu,finalNeg=neg, text=text, text_no_processing=text_no_processing, compound=compound)
    elif compound <= -0.05:
        return render_template('index.html', final=neg,finalP=pos,finalNeu=neu,finalNeg=neg, text=text, text_no_processing=text_no_processing, compound=compound)
    else:
        return render_template('index.html', final=neu,finalP=pos,finalNeu=neu,finalNeg=neg, text=text, text_no_processing=text_no_processing, compound=compound)

"""
@app.route('/Ml_model')
def index():
    df = pd.read_csv('moviereviews.tsv', sep ='\t')
    df_table = df.head()
    df.dropna(inplace=True)
    blanks = []
    for i,lb,rv in df.itertuples():
        if type(rv)==str:
            if rv.isspace():
                blanks.append(1)
    df.drop(blanks, inplace=True)
    analyser = SentimentIntensityAnalyzer()
    df['scores']= df['review'].apply(lambda review: analyser.polarity_scores(review))
    df['compound']= df['scores'].apply(lambda score: score['compound'])
    df['com_score']= df['compound'].apply(lambda c: 'pos' if c >=0 else 'neg')
    accuracy_score = accuracy_score(df['label'],df['com_score'])
    return render_template('model.html', accuracy_score=accuracy_score)

"""
