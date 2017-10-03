import re,json
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

def clean_html(html):
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    cleaned = re.sub(r"&nbsp;", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    return (((((cleaned.rstrip())).replace('\\n',' ')).replace('\\r',' ')).replace('\\t',' '))

def Pre_Process(html):
    string=""
    text = clean_html(html)
    terms = re.findall(r'\w+',text)
    terms=[term for term in terms]
    stemmer = SnowballStemmer("english")
    for item in terms:
        if item not in stopwords.words('english'):
            item=stemmer.stem(item)
            string+=str(item+" ")
    return string

json1_file = open('Main.json')
json1_str = json1_file.read()
file1=open("URL_main.csv","a")
file2=open("Title_main.csv","a")
file3=open("Pre_Title.csv","a")
file4=open("Body_main.csv","a")
file5=open("Pre_Body.csv","a")
for i in range(0,len(json1_str)-1):
    json1_data = json.loads(json1_str)[i]
    a=(dict(json1_data))
    file1.write(str(i)+","+a['url']+"\n")
    file2.write(str(i)+","+repr(a['title'])+"\n")
    file3.write(str(i)+","+Pre_Process(repr(a['title']))+ "\n")
    file4.write(str(i)+","+repr(a['body'])+"\n")
    file5.write(str(i)+","+Pre_Process(repr(a['body']))+"\n")
    print(str(i) + " " + str(a['url']))
file1.close()
file2.close()
file3.close()
file4.close()
file5.close()