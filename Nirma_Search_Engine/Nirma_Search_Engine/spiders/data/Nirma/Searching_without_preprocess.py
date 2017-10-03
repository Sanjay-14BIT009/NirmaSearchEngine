# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:28:09 2017

@author: Abc
"""

import re,sys,csv
from timeit import default_timer as timer
 
maxInt = sys.maxsize
decrement = True

def searchWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

word = input()

while decrement:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

file=open("Body_main.csv" , 'rt')
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