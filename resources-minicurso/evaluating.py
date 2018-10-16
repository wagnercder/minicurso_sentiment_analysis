import csv
import pickle
import sys
import nltk


def search_words(text): #procura por uma palavra em específico
    all_words = []

    for(words, emotion) in text:
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

c = open('bases/my_classifier.pickle', 'rb')

with open("bases/eval_base_sememote.csv", "r", newline = '', encoding = 'utf-8') as csv_file:
    data_list =  csv.reader(csv_file)
    base = []
    
    for (item, emocao) in data_list:
        base.append((item.split(),emocao))
    
    frequency = search_frequency(search_words(base))
    
    unique_words = search_uniq_words(frequency)

    classifier = pickle.load(c) 

    base = nltk.classify.apply_features(extract_words, base)

    print('\n#### ACURACIA ####')
    print(nltk.classify.accuracy(classifier, base))

    c.close()