import csv
import nltk
import re
import sys
import pickle

from nltk.metrics import ConfusionMatrix

def search_words(text): #procura por uma palavra em específico
    all_words = []

    for(words, emocao) in text:
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

f = open("bases/preprocessed_training_base.csv", "r", newline = '', encoding = 'utf-8')
g = open("bases/classified_base.csv", "r", newline = '', encoding = 'utf-8')
c = open('bases/my_classifier.pickle', 'rb')

file_train_base = csv.reader(f)
file_class_base = csv.reader(g)

base_train = []
base_class = []

for (item, emocao) in file_train_base:
    base_train.append((item.split(),emocao))

for (item, emocao) in file_class_base:
    base_class.append((item.split(),emocao))    

unique_words_class = search_uniq_words(search_frequency(search_words(base_class)))
unique_words = search_uniq_words(search_frequency(search_words(base_train)))

basecompletatreinamento = nltk.classify.apply_features(extract_words, base_train)
basecompletateste = nltk.classify.apply_features(extract_words, base_class)

esperado = []
previsto = []

classifier = pickle.load(c) 

for (frase, classe) in basecompletateste:
    resultado = classifier.classify(frase)
    previsto.append(resultado)
    esperado.append(classe)

print('\n### CONFUSION MATRIX ###\n')

matriz = ConfusionMatrix(esperado, previsto)

print(matriz)

sys.exit()