import pytest
import app
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score,classification_report

def test_vader_model():
    df = pd.read_csv('moviereviews.tsv', sep ='\t')
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
    assert (accuracy_score(df['label'],df['com_score'])) > 80

analyser = SentimentIntensityAnalyzer()
sentence = 'this kitchen is delicious'
sentence2 = 'this kitchen is DELICIOUS'
sentence3 = 'this kitchen is delicious !!!!'
sentence4 = 'this kitchen is DELICIOUS !!!!'
text = analyser.polarity_scores(sentence)
text2 = analyser.polarity_scores(sentence2)
text3 = analyser.polarity_scores(sentence3)
text4 = analyser.polarity_scores(sentence4)

def test_accuracy_text_lower():
    assert text['compound'] > text2['compound']

def test_accuracy_text_pounctuation():
    assert text['compound'] < text3['compound'] < text4['compound']

