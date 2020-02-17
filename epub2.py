import requests
from lxml import html

pageContent=requests.get(
     'file:///Users/akrati/Desktop/AMAZON/3cepx-miyxy/3cepx-miyxy_files/OEBPS/Text/Chapter%201.html'
)
tree = html.fromstring(pageContent.content)

