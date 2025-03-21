# -*- coding: utf-8 -*-
"""AD8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17CHY5MSBUpbYm2TjBRZBPqhVvvjioyx7
"""

from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pickle
from sklearn.linear_model import LogisticRegressionCV
import re
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('/content/covid_fake.csv')
df.head()

df.shape

df['label'].value_counts()

df.loc[5:15]

