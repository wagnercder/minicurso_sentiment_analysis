import sys
import matplotlib.pyplot as plt
import re
import csv

def show_graphic_training_base():
    with open('bases/preprocessed_training_base.csv', 'r', newline = '', encoding = 'utf-8') as csvfile:
        data = csv.reader(csvfile)
        positive = 0
        neutral = 0
        negative = 0

        for item in data:
            if item[1] == 'positive':
                positive += 1
            if item[1] == 'neutral':
                negative += 1
            if item[1] == 'negative':
                neutral += 1

        labels = 'Positive', 'Negative', 'Neutral'
        sizes = [positive, negative, neutral]
        
        explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()

def show_graphic_classified_base():
    with open('bases/classified_base.csv', 'r', newline = '', encoding = 'utf-8') as csvfile:
        data = csv.reader(csvfile)
        positive = 0
        neutral = 0
        negative = 0

        for item in data:
            if item[1] == 'positive':
                positive += 1
            if item[1] == 'neutral':
                negative += 1
            if item[1] == 'negative':
                neutral += 1

        labels = 'Positive', 'Negative', 'Neutral'
        sizes = [positive, negative, neutral]
        
        explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()    

show_graphic_classified_base()
#show_graphic_training_base()
    
    