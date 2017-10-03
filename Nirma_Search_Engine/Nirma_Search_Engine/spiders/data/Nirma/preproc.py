# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:31:25 2017

@author: Dell
"""

import re,json
from bs4 import BeautifulSoup
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

class search_engine():
    
    def removeScriptCSS(self,html):
        soup = BeautifulSoup(html,"html5lib") 
        for script in soup(["script", "style"]): 
            script.extract()
        text = str([text for text in soup.stripped_strings])
        return text

    def preprocess(self,text):
        string=""
        text=((((((text.replace("\\r"," ")).replace("\\t"," ")).replace("\\t"," ")).replace("\\n"," ")).replace("\\"," ")).replace("<br />"," ")).replace("_"," ")
        freetext=self.removeScriptCSS(text)
        terms = re.findall(r'\w+',freetext)
        terms=[term for term in terms]
        stemmer = SnowballStemmer("english")
        for item in terms:
            if item not in stopwords.words('english'):
                item=stemmer.stem(item)
                string+=str(item+" ")
        return string
    
    def main(self):
        json1_file = open('Main.json')
        json1_str = json1_file.read()
        file1=open("Pre_Title1.csv","a")
        file2=open("Pre_Body1.csv","a")
        file3=open("original_title.csv","a")
        file4=open("original_body.csv","a")
        file5=open("Pre_URL1.csv","a")
        for i in range(0,len(json1_str)-1):
            json1_data = json.loads(json1_str)[i-1]
            a=(dict(json1_data))
            body=a['body']
            title=a['title']
            url=a['url']
            print(str(i)+" "+url)
            print(str(i)+" , "+repr(title).rstrip()+"\n")
            print(str(i)+" , "+repr(self.preprocess(title)).rstrip()+"\n")
            print(str(i)+" , "+repr(body).rstrip()+"\n")
            print(str(i)+" , "+repr(self.preprocess(body)).rstrip()+"\n")
            #file5.write(str(i)+" , "+url+"\n")
            if(i==len(json.loads(json1_str))):
                break
        file1.close()
        file2.close()
        file3.close()
        file4.close()
        file5.close()
        
            
if __name__=='__main__':                       
    k=search_engine()
    k.main() 