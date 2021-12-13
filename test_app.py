import pytest
import requests
import app
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score,classification_report
import json
from bs4 import BeautifulSoup as BS

def test_site_is_working():
	assert requests.get('http://localhost:5000').status_code == 200


def test_with_only_positive_words():
	dataToSend = {'text': 'happy glad'}
	x = requests.post('http://localhost:5000', data = dataToSend)
	soup = BS(x.text, 'html.parser')
	input_tag = soup.find(attrs={"id": "pos"}).getText()
	output = float(input_tag)
	print(output)
	assert output == 100.00


def test_with_only_negative_words():
	dataToSend = {'text': 'sad destroying '}
	x = requests.post('http://localhost:5000', data = dataToSend)
	soup = BS(x.text, 'html.parser')
	input_tag = soup.find(attrs={"id": "neg"}).getText()
	output = float(input_tag)
	print(output)
	assert output == 100.00

def test_with_only_neutral_words():
	dataToSend = {'text': 'of with'}
	x = requests.post('http://localhost:5000', data = dataToSend)
	soup = BS(x.text, 'html.parser')
	input_tag = soup.find(attrs={"id": "neut"}).getText()
	output = float(input_tag)
	print(output)
	assert output == 100.00

def test_site_can_handle_stress():
	seconds = 0.0
	for i in range(1000):
		response = requests.get("http://localhost:5000")
		seconds+=response.elapsed.total_seconds()
	assert seconds < 100
	

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













