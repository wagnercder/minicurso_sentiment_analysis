#  -*- coding: utf-8 -*-
import csv
import pickle
import sys
import nltk

def search_words(texto): #procura por uma palavra em específico
    all_words = []

    for(palavras, emocao) in texto:
        all_words.extend(palavras)

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

def show_features_training_data():
    c = open('bases/my_classifier.pickle', 'rb')

    classifier = pickle.load(c) 

    print('\n####### CATEGORIAS ########')
    print(classifier.labels())

    print('\n####### PALAVRAS MAIS IMPORTANTES ########')
    print(classifier.show_most_informative_features(10))

    c.close()

#Treinamento da base de classificação
with open('bases/preprocessed_training_base.csv', 'r', newline = '', encoding = 'utf-8') as csvfile:
    text = csv.reader(csvfile)
    base = []

    for item in text:
        base.append((item[0].split(), item[1]))

    frequency = search_frequency(search_words(base))
    
    unique_words = search_uniq_words(frequency)

    base = nltk.classify.apply_features(extract_words, base)
    classifier = nltk.NaiveBayesClassifier.train(base) #monta a tabela de probabilidades

    f = open('bases/my_classifier.pickle', 'wb')
    
    pickle.dump(classifier,f )
    
    f.close()
