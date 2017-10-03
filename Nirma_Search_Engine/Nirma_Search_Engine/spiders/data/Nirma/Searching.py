# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:28:09 2017

@author: Abc
"""

import re,sys,csv
from timeit import default_timer as timer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
 
maxInt = sys.maxsize
decrement = True

def Pre_Process(data):
    string=""
    terms = re.findall(r'\w+',data)
    terms=[term for term in terms]
    stemmer = SnowballStemmer("english")
    for item in terms:
        if item not in stopwords.words('english'):
            item=stemmer.stem(item)
            string+=str(item+" ")
    return string

word = input()
word = Pre_Process(word)

def searchWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

while decrement:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

file=open("Pre_Body.csv" , 'rt')
reader = csv.reader(file)

docList = set()

start = timer()
for row in reader:
    data = row
    
    if(searchWord(word)(data[1])):
        docList.add(int(data[0]))
        
end = timer()
    
file.close()

docList = sorted(docList)

file=open("URL_main.csv" , 'rt')
reader = csv.reader(file)

lineNo = 0

for row in reader:
    data = row
    
    if(lineNo in docList):
        print(data[1])
    
    lineNo += 1
    
print("Number of Records Retrieved : " + str(len(docList)) + "\n")
print(end-start)
    
file.close()