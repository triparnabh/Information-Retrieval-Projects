import os
import re
from nltk.stem import PorterStemmer
from collections import Counter
import string

global final
final=[]
word_list=[]
pattern = r"<TEXT>(.*?)</TEXT>"
pattern2 = r"<TITLE>(.*?)</TITLE>"

punctuations='!"#$%&\'()\\n*+,-./:;<=>?@[\\]^_`{|}~'
#punctuations = string.punctuation
reg_pattern = '[' + punctuations + ']'

directory= "cranfieldDocs/"

for file in os.listdir(directory):
    with open(directory + file, 'r') as vocab:
        word_list = str(re.findall(pattllllern, str(vocab), flags=re.DOTALL) + re.findall(pattern2, str(vocab), flags=re.DOTALL))
        print word_list

"""for line in x:
            
            for word in line.split():
                y = re.sub(reg_pattern, '', word).lower()
                word_list.append(y)


s = str (re.findall(pattern, word_list, flags=re.DOTALL) + re.findall(pattern2, word_list, flags=re.DOTALL))
s= s.replace('\\n','')

print s

stemmer = PorterStemmer()

stop_words = []
f = open("stopwords.txt") # the stopwords list provided in the assignment1
stop_words = f.read().splitlines()

def main():

    for word in s.split():
        y = re.sub(reg_pattern, '', word).lower()
        y = stemmer.stem(y)
        if (y != "") & (len(y)>2) & (y.isdigit()==False):
            if y not in stop_words:
                y = y.strip("\\n")
                final.append(str(y))
    print final

def inverted_index():
    di = {}
    for k in final:
        if k in di:
            di[k]['0001'] = di[k]['0001'] + 1

        else:
            di[k] = {}
            di[k]['0001'] = 1

    print ('New dictionary', di)

main()
inverted_index()"""
