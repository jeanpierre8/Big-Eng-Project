import pytest
import pandas as pd
import numpy as np
import nltk
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

nltk.download('stopwords')
stop_words = stopwords.words("english")
stemmer = SnowballStemmer("english")

def preprocess(text, stem=False):
    text = re.sub("@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+", ' ', str(text).lower()).strip()
    tokens = []
    for token in text.split():
        if token not in stop_words:
            if stem:
                tokens.append(stemmer.stem(token))
            else:
                tokens.append(token)
    return " ".join(tokens)

dff = pd.read_csv('moviereviews.tsv', sep ='\t')
tfidf = TfidfVectorizer(analyzer=preprocess)
XX = dff['review'].values.astype('U')
yy = dff['label']
XX= tfidf.fit_transform(XX)
XX_train, XX_test, yy_train, yy_test = train_test_split(XX,yy,test_size=0.2, random_state=0)
loaded_model = pickle.load(open('custom_model', 'rb'))
result = loaded_model.score(XX_test, yy_test)
result = result * 100

def test_model_accuracy():
    assert result > 100