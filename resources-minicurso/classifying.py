#  -*- coding: utf-8 -*-
import csv
import pickle
import sys
import nltk

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

d = open('bases/classified_base.csv', 'w+', newline = '', encoding = 'utf-8')
f = open('bases/my_classifier.pickle', 'rb')

#Classificação de uma sentença única pra teste
with open('bases/preprocessed_base.csv', 'r', newline = '', encoding = 'utf-8') as csvfile:
    text = csv.reader(csvfile)
    base = []
        
    classifier = pickle.load(f)
    constem = []
    
    for palavras in text:
        comstem = [p for p in palavras[0].split()]
        
        base.append(comstem)
    
    frequency = search_frequency(search_words(base))
    unique_words = search_uniq_words(frequency)

    for item in base:
        nova_base = extract_words(item)
        d.write(turn_back_string(item) + ',' + classifier.classify(nova_base)+ '\n')

d.close()
f.close()
sys.exit()