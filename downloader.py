import requests
from bs4 import BeautifulSoup as bs
import urllib2
import os
from io import open

_URL= ""
_URL_BASE = ""
_HDR = {'User-Agent': 'Mozilla/5.0'}
# functional
r = requests.get(_URL)
soup = bs(r.text)
urls = []
names = []

print(soup)

urls = []
links = []
for i, link in enumerate(soup.findAll('a')):
    _FULLURL = _URL_BASE + link.get('href')
    if _FULLURL.endswith('.pdf'):
        urls.append(_FULLURL)
        names.append(soup.select('a')[i].attrs['href'])

names_urls = zip(names, urls)

for name, url in names_urls:
    print url
    name_string = "pdfs/" + name
    rq = urllib2.Request(url, headers=_HDR)
    res = urllib2.urlopen(rq)
    if not os.path.exists(os.path.dirname(name_string)):
        os.makedirs(os.path.dirname(name_string))
    pdf = open(name_string, 'wb')
    pdf.write(res.read())
    pdf.close()

