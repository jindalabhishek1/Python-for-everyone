# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
# Sample: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Actual: http://py4e-data.dr-chuck.net/known_by_Rehan.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

# Retrieve all of the anchor tags
# print(type(tags))
# print(tags[pos-1])

names = []
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    names.append(tags[pos-1].contents[0])
    url = tags[pos-1].get('href', None)
    #print(tag.get('href', None))
print (names[count-1])
