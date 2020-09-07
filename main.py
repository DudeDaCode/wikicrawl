import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import sys

topic = input("Enter Your Topic : ")
link = f'http://en.wikipedia.org/wiki/{topic}'
source = urlopen(link).read()
 
soup = BeautifulSoup(source,'lxml')
soup

paras = []
for paragraph in soup.find_all('p'):
    paras.append(str(paragraph.text))

heads = []
for head in soup.find_all('span', attrs={'mw-headline'}):
    heads.append(str(head.text))

text = [val for pair in zip(paras, heads) for val in pair]
text = ' '.join(text)

text = re.sub(r"\[.*?\]+", '', text)

text = text.replace('\n', '')[:-11]
print(text)
