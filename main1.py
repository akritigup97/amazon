from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pyPdf
import re
import csv 
def getPDFContent(path):
    stop_words=set(stopwords.words("english"))
    stop_words.update(('also','helps','role','depend'))
    ps= PorterStemmer()
    content = ""
    reg="^[a-zA-Z]+$"
    a=set()
    dic={}
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    for i in range(0,1):##pdf.getNumPages()
        ##f=open("xxx.txt",'a')
        content= pdf.getPage(i).extractText() + "\n"
        import string
        c=word_tokenize(content)
        for b in c:
            
            ##f.write(" ")
            b = b.encode('utf-8').lower()
            
            if b not in stop_words:
                if re.match(reg, b): 
                    ##f.write(b)
                    a.add(b)
               
        ##f.write("\n")
        
        ##f.close()
    ##print (a)
 ##   dic={'solidstates':list(a)}
                    
    dic['state solid']= list(a)
    print (dic)
    
    
    
    with open('log.csv', 'w') as out_file:
        writer = csv.writer(out_file,delimiter=' ',)
        writer.writerow(('title', 'intro'))
        writer.writerows(list(a))
    return 0
    
print getPDFContent("chem101.pdf")
