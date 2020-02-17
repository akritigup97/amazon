from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
examle = "it is a big thing for me and the entire world we need to move forward and lead the world"
stop_words=set(stopwords.words("english"))
words=word_tokenize(examle)
ps= PorterStemmer()
filter=[]
for w in words:
    if w not in stop_words:
        filter.append(w)
        
for v in filter:
    print(ps.stem(v))

