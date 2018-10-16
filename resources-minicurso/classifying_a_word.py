#  -*- coding: utf-8 -*-
import csv
import pickle
import sys
import nltk
import emoji
import re

from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords 

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

def search_words(text): #procura por uma palavra em específico
    all_words = []

    for(words) in text:
        all_words.extend(words)

    return all_words

def search_frequency(words): #retorna a frequência em que as palavras estão distribuídas
    words = nltk.FreqDist(words)

    return words

def search_uniq_words(frequency_words): #usada para verificar palavras únicas e n duplicadas
    return frequency_words.keys()

def extract_words(documento): #verifica se uma palavra existe ou não em uma frase/documento
    doc = set(documento)
    caracteristicas = {}
    for palavras in unique_words:
        caracteristicas['%s' % palavras] = (palavras in doc)
    
    return caracteristicas

def turn_back_string(split_text):
    complete_word = ''
    
    for word in split_text:
        complete_word = complete_word + ' ' + word
    
    return complete_word

f = open('bases/my_classifier.pickle', 'rb')

sentence = 'I hate @VirginAmerica'
test_text = preprocessing(sentence)

#Classificação de uma sentença única pra teste
with open('bases/preprocessed_base.csv', 'r', newline = '', encoding = 'utf-8') as csvfile:
    text = csv.reader(csvfile)
    base = []

    word_array = []

    classifier = pickle.load(f)

    for palavras in text:
        base.append([p for p in palavras[0].split()])

    frequency = search_frequency(search_words(base))
    unique_words = search_uniq_words(frequency)

    for item in test_text.split():
        word = [p for p in item.split()]
        word_array.append(word[0])

    word = extract_words(word_array)
    
    print('\n' + sentence + ' - ' + classifier.classify(word))
    
    distribuicao = classifier.prob_classify(word)
    
    print('\n### PROBABILIDADE POR CATEGORIA ###\n')
    for classe in distribuicao.samples():
        print("%s: %f" % (classe, distribuicao.prob(classe)))

    f.close()