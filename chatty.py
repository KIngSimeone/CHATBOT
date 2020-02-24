import nltk
import numpy as np
import random
import string



f=open('chatbot.txt', 'r', errors = 'ignor')

raw=f.read
raw = raw.lower()

nltk.download('punkt')
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatize()

def LemTokens(tokens):
    return [lemmer.lemmatize(token)for token in tokens]

remove_punct_dict = dict((ord(punct),None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))




GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)

GREETING_RESPONSES = ["hi","hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"

def greeting(sentence):

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)