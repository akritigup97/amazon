from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
examle = "helloo how are you doing today?weather is awesome"
stop_words=set(stopwords.words("english"))
stop_words.update(('know','helps','gets','akriti'))
print(stop_words)
