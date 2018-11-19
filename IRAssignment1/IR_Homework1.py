# Name:- Triparna Bhattacharya, CS 582 Homework1

import os
import string
import regex as re
from nltk.stem import PorterStemmer
import operator

file_path = "citeseer/"
punctuations = string.punctuation
reg_pattern = '[' + punctuations + ']'
di = dict()

def function1(x):
                for word in x:
                    y = re.sub(reg_pattern, '', word).lower()
                    if y != "":
                            if y in di:
                                di[y] = di[y] + 1
                            else:
                                di[y] = 1
                            #print (y, di[y])

def total_words(): # summing the frequency i.e the value of each key in the dictionary
    sum = 0

    for key, value in di.iteritems():
        sum += value
    print 'Question a. Total number of words:',sum

def unique_words(): # calculating the total number of keys in the dictionary which is actually the unique word count

    print 'Question b. Total number of unique words:', len(di)

def top_20_words1():
    global top_20_words
    top_20_words = []
    global frequency_sorted
    frequency_sorted={}
    frequency_sorted = sorted(di.items(), key = operator.itemgetter(1), reverse=True)   # sorting the  words in reverse order with highest frequency
                                                                                         #print frequency_sorted
    print type(frequency_sorted)
    k=1

    print ('Question c: Top twenty frequent words:')
    for i in frequency_sorted:
        w=""
        if k <= 20:
            w=str(i[0])+" : "+str(i[1])
            print(w)
            k=k+1
            top_20_words.append(i)

stop_words = []
f = open("stopwords.txt") # the stopwords list provided in the assignment
stop_words = f.read().splitlines()

def find_stop_words():

    top20_stop_words = []
    total_frequency = 0
    x=0
    words = 0

    for key, value in di.iteritems():
        total_frequency = total_frequency + value

    fifteen = (total_frequency*15)/100

    for k in top_20_words:
        if k[0] in stop_words:
               top20_stop_words.append(k[0])

    for k in frequency_sorted:
        if x <= fifteen:
                   x= x+ int(k[1])
                   words = words + 1

    print 'Question d. Stop-words in top 20:', top20_stop_words
    print 'Question e. Total words accounting to 15% of vocabulary:', words


def main():
    global word_list, di
    word_list = []

    for file in os.listdir(file_path):
        with open(file_path + file, 'r') as x:
            for line in x:
                for word in line.split():
                    y = re.sub(reg_pattern, '', word).lower()
                    word_list.append(y)
    function1(word_list)
    total_words()
    unique_words()
    top_20_words1()
    find_stop_words()

    di = {}
    stemmed_word_list = []
    stemmer = PorterStemmer()
    for word in word_list:
        if word not in stop_words:
            stem_word = stemmer.stem(word)
            stemmed_word_list.append(stem_word)

    print ("With Porter Stemmer")
    function1(stemmed_word_list)
    total_words()
    unique_words()
    top_20_words1()
    find_stop_words()


main()


