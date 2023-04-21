import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
nltk.download('stopwords')
import pickle

import string
from nltk.corpus import stopwords

def text_process(mess):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    STOPWORDS = stopwords.words('english') + ['u', 'ü', 'ur', '4', '2', 'im', 'dont', 'doin', 'ure']
    # Check characters to see if they are in punctuation
    nopunc = [char for char in mess if char not in string.punctuation]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    
    # Now just remove any stopwords
    return ' '.join([word for word in nopunc.split() if word.lower() not in STOPWORDS])

def predict(text):
   
    text=text_process(text)

    with open('controller/models/vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    with open('controller/models/model.pkl', 'rb') as f:
        model = pickle.load(f)
    new_data = vectorizer.transform([text])
    predicted_class = model.predict(new_data)
    return predicted_class[0]