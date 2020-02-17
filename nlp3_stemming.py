from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps= PorterStemmer()
examle = ["python","pythonner","pythonnier","pythonme","pythoniw"]
#for w in examle:
#    print(ps.stem(w))
exampl2="it is a big thing for me and the entire world we need to move forward and lead the world"
words=word_tokenize(exampl2)
for v in words:
    print(ps.stem(v))
