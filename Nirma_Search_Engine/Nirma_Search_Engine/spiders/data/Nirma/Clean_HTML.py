 # -*- coding: utf-8 -*-

import re
import csv
import nltk
from nltk.corpus import stopwords,names
from nltk.stem.lancaster import LancasterStemmer

def clean_html(html):
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    cleaned = re.sub(r"&nbsp;", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    return cleaned.strip()
    raise NotImplementedError ("To remove HTML markup, use BeautifulSoup's get_text() function")
    
def tokenize(self,text):
    terms = re.findall(r'\w+', text) 
    terms = [term for term in terms if not term.isdigit()] 
    #print(terms)
    return terms

def frequency(self,text):
    sent=self.tokenize(text)
    string=""
    for i in sent:
        if i not in stopwords.words('english')+names.words():
            las=LancasterStemmer()
            temp=las.stem(i)
            lemma = nltk.wordnet.WordNetLemmatizer()
            lemma.lemmatize(temp)
            string+=str(temp+" ")
                    
    return string

fileT=open("Title_new.csv")
corpus = csv.reader(fileT)
fileTPre=open("Title_new_Pre.csv","a")

a = 1

for row in corpus:
    data = row
    data[1]=((data[1].replace('\\n',' ')).replace('\\t',' ')).replace('\\r' ,' ');
    fileTPre.write(str(data[1])+"\n")
    #soup = clean_html(data[1])
    #soup = clean_html(soup)
    #print(soup)
    terms = re.findall(r'\w+' , data[1])
    terms = [term for term  in terms if not term.isdigit()]
    print(terms)
    
    if(a == 10):
        break
    
    a += 1
'''a = 1

for row in reader:
    a = a + 1
    print(row)
    #soup = clean_html(row)
    #print(soup)
    
    if(a==2):
        break'''
    
fileTPre.close()
fileT.close()   