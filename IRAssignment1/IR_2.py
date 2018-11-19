import os
import string
import regex as re
import pandas as pd
import nltk
import nltk.corpus
from nltk.stem import PorterStemmer

#nltk.download('stopwords')
import collections

file_path = "citeseer/"
punctuations = string.punctuation
reg_pattern = '[' + punctuations + ']'

arr = []

def main():
    for file in os.listdir(file_path):
        with open(file_path + file, 'r') as x:
            for line in x:
                for word in line.split():
                    y = re.sub(reg_pattern, '', word)

                    if y != "":
                        # print y.strip()
                        arr.append(y)

    df = pd.DataFrame({'list_words': arr})
    global global_word_list
    global_word_list = pd.DataFrame(df)
    # print df

    # arr.append(re.sub('[' + punctuations + ']', " ", word))


def query1():
    size = global_word_list.size
    print 'Total number of words in collection:', size


def query2():
    global df
    df = global_word_list['list_words'].unique()
    print 'Unique vocabulary size:', df.size


def query3():
    global top_20
    top_20 = []
    df = global_word_list
    df['frequency'] = df.groupby('list_words')['list_words'].transform('count')

    # counts = df['list_words'].value_counts().to_dict()
    # top_20_words = collections.Counter(counts)
    # print top_20_words.most_common(20)

    print df
    top_20 = df.sort_values('frequency', ascending=False).drop_duplicates(subset=['list_words', 'frequency'],keep='first').head(20)
    print ('Top 20 words with highest frequency:')
    print (top_20)


def query4():
    global stop_words
    stop_words = []
    top20_stop_words = []

    f = open("stopwords.txt")
    stop_words = f.read().splitlines()
    # print stop_words

    for index, row in top_20.iterrows():
        if row['list_words'] in stop_words:
            top20_stop_words.append (row['list_words'])

    print 'Stop-words in top 20:', top20_stop_words

def query5():

    total_frequency=0
    sum=0
    cut_off_percent=0

    df = global_word_list
    unique_vocab = df.sort_values('frequency', ascending=False).drop_duplicates(subset=['list_words', 'frequency'],keep='first')
    for index, row in unique_vocab.iterrows():
        total_frequency = total_frequency + row['frequency']
    print('***************************')
    #print unique_vocab

    for index, row in unique_vocab.iterrows():
        #total_frequency = total_frequency + row['frequency']
        sum= sum+row['frequency']
        cut_off_percent = (sum * 100)/total_frequency
        print ('Words accounting for 15% of collection:', row['list_words'])
        if cut_off_percent > 15:
            break



def porter_stemmer_function():
    stemmer = PorterStemmer()
    arr2 =[]
    df = global_word_list
    for index, row in df.iterrows():
        arr2.append(stemmer.stem(row['list_words']))
    #print arr2.size

    stemmed_dataframe = pd.DataFrame({'list_words': arr2})
    #print('=========================================')
    #print stemmed_dataframe
    print ('Size of stemmed vocabulary:', stemmed_dataframe.size)
    stemmed_unique = (stemmed_dataframe['list_words'].unique())
    print ('Size of stemmed unique vocabulary:', stemmed_unique.size)
    top_20_stemmed = stemmed_dataframe.sort_values('frequency', ascending=False).drop_duplicates(subset=['list_words', 'frequency'], keep='first').head(20)
    print ('Top 20 words with highest frequency:')
    print (top_20_stemmed)


    #for x in stemmed_unique:
        #print"""


main()
query1()
query2()
query3()
query4()
query5()
porter_stemmer_function()
