##https://www.aconvert.com/file.php
from ebooklib import epub
##book=epub.read_epub('chem1.epub')
##print book
from urllib2 import urlopen
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pyPdf
import re
import csv 
html=urlopen("file:///Users/akrati/Desktop/AMAZON/3cepx-miyxy/3cepx-miyxy_files/OEBPS/Text/Chapter%201.html")
bsOb = BeautifulSoup(html.read())
subhead= bsOb.findAll("",{"class":"calibre13"})
subsubhead= bsOb.findAll("p",{"class":"subheading1"})
subsubhead1= bsOb.findAll("p",{"class":"subheading3"})
subsubhead.extend(subsubhead1)
key1=bsOb.findAll("p",{"class": "calibre8"})
head=bsOb.findAll("h2",{"class":"calibre6"})
d={}
l=[]
stop_words=set(stopwords.words("english"))
stop_words.update(('also','helps','role','depend'))
ps= PorterStemmer()
content = ""
reg="^[a-zA-Z]+$"
a=set()
for c in subhead:
    
    b= c.get_text()
    b.lower()
    if b not in stop_words:
       a.add(b)
'''for n in head:
    print(n.get_text())
    for y in subhead:
         l.append(y.get_text())
         d[n.get_text()]=l       
 


for name in subhead:
    p=name.get_text()
    l=[]
    for y in subsubhead:
        h=y.get_text()
        
    d[p]= l
    
    '''
print(a)
