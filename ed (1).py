# -*- coding: utf-8 -*-
"""ED.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VkbEDqhjgYbjNz2JOsEZe7tv-w55teDx
"""

import pandas as pd

df = pd.read_csv("/content/emotion.csv")
df.head()

df.shape

df.info()

df.isna().sum()

df.label.value_counts()

import seaborn as sns
sns.countplot(x=df.label)

df['text']=df['text'].apply(lambda x: " ".join(x.lower() for x in x.split()))

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop=stopwords.words('english')
df['text']=df['text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

pip install textblob

from nltk.stem import WordNetLemmatizer
from textblob import Word
import nltk
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

df['text'] = df['text'].apply(lambda x: " ".join([lemmatizer.lemmatize(word) for word in x.split()]))
df['text'].head()

X = df['text']
y = df['label']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print(X_train.shape , y_train.shape)

print(X_test.shape , y_test.shape)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
tfidf.fit(df['text'])
xtrain_tfidf = tfidf.transform(X_train)
xtest_tfidf = tfidf.transform(X_test)

from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn import metrics
pclf = PassiveAggressiveClassifier()
pclf.fit(xtrain_tfidf, y_train)
pred = pclf.predict(xtest_tfidf)
print( metrics.classification_report(y_test, pred))

























