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
subhead= bsOb.findAll("",{"class":"calibre8"})

d={}

stop_words=set(stopwords.words("english"))
stop_words.update(('also','helps','role','depend'))
ps= PorterStemmer()
content = ""
reg="^[a-zA-Z]+$"
a=set()

for c in subhead:
    children=c.findChildren()
    for child in children:
        print child
    #for p in bsOb.find(c).parent.find_next_siblings():
        #print(p.get_text())
   # b= c.get_text()
 #   key1=bsOb.findNext("p",{"class": "calibre8"})
 #   a.add(b)
    
print(a)

