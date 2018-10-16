#  -*- coding: utf-8 -*-
import csv
import re
import emoji
import nltk
import sys
import pickle

from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords 

#Remover emoticon [X]
#Remover Link [X]
#Remover Citação @fulano [X]
#Remover símbolos ou pontuações [X]
#Remover stopwords [X]
#Maiúsculo vira minúsculo [X] text.lower()
#Processo de Stemming [X]

#Métodos pré-processamento
def preprocessing(text):
    return remove_stopwords(remove_symbols(remove_citation_tweet(remove_link(remove_emoji(text)))).lower())

def remove_emoji(text):
    return emoji.get_emoji_regexp().sub(u'', text)

def remove_link(link):
    return re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', link)
    
def remove_citation_tweet(citation):
    return re.sub(r'@[A-Za-z0-9]+', '', citation)

def remove_symbols(text):
    return re.sub('[^\w][0-9]*', ' ', text)
    
def remove_stopwords(sentence):
    auxword = ''
    
    for word in sentence.split():
        if word not in stopwords.words('english'):
            auxword = auxword + ' ' + word

    return auxword

def stemming(sentence):
    stemmer = SnowballStemmer('english') #steemer usado especificamente para o inglês
                                         #nltk.corpus.stopwords.words('portuguese') stemming para português
    auxword = ''

    for word in sentence.split():
        auxword = auxword + " " + str(stemmer.stem(word))

    return auxword

def examplePreprocessing(text):
    print (text)
    text = remove_emoji(text)
    print(text)
    text = remove_link(text)
    print(text)
    text = remove_citation_tweet(text)
    print(text)
    text = remove_symbols(text)
    print(text)
    text = text.lower()
    print(text)
    text = remove_stopwords(text)
    print(text)
    text = stemming(text)
    print(text)

#examplePreprocessing('I ❤️ flying @VirginAmerica. And I ! ❤️ @trip on https://facebook.com.br')
examplePreprocessing('I flying @VirginAmerica. And I !  @trip on https://facebook.com.br')

f = open("bases/preprocessed_base.csv", "w+", newline = '', encoding = 'utf-8')

with open('bases/tweets.csv', 'r', newline = '', encoding = 'utf-8') as csvfile:
    text = csv.reader(csvfile)
    
    for item in text:
        text = stemming(preprocessing(item[0]))
        if not text.strip(): continue
        f.write(text + '\n')

    f.close

