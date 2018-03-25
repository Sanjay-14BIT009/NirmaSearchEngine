from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import re, sys, csv
from timeit import default_timer as timer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords


def Pre_Process(data):
    string = ""
    terms = re.findall(r'\w+', data)
    terms = [term for term in terms]
    stemmer = SnowballStemmer("english")
    for item in terms:
        if item not in stopwords.words('english'):
            item = stemmer.stem(item)
            string += str(item + " ")
    return string


def searchWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def index(request):
    return render(request, 'Main/home.html')


def Search(request, que):
    Query = request.POST['query']
    word = Pre_Process(Query)

    maxInt = sys.maxsize
    decrement = True

    while decrement:

        decrement = False
        try:
            csv.field_size_limit(maxInt)
        except OverflowError:
            maxInt = int(maxInt / 10)
            decrement = True

    i = 0

    for term in re.findall(r'\w+', word):
        print(term)
        file = open("Main/Pre_Body.csv", 'rt')
        reader = csv.reader(file)
        docList = set()
        start = timer()
        for row in reader:
            data = row
            if searchWord(term)(data[1]):
                docList.add(int(data[0]))
        end = timer()
        if i == 0:
            doc = docList
            i = 1
        if i != 0:
            doc = list(set(doc).intersection(sorted(docList)))
        print(docList)
        print(doc)
        file.close()

    docList = sorted(doc)

    file = open("Main/URL_main.csv", 'rt')
    reader = csv.reader(file)

    lineNo = 0

    output="";

    for row in reader:
        data = row

        if (lineNo in docList):
            output+="<a href='" + data[1] + "'>" + data[1] + "</a><br>"

        lineNo += 1

    output+="<br><h3>Number of Records Retrieved : " + str(len(docList)) + "<h3><br>"
    output+="<h3>Time Elapsed : " + str(end-start) + "</h3>"

    file.close()

    return HttpResponse(output)