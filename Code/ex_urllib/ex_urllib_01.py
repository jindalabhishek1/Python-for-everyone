# Sample data: http://py4e-data.dr-chuck.net/comments_42.html
# Actual data: http://py4e-data.dr-chuck.net/comments_888985.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
count = 0
tags = soup('span')
for tag in tags:
    num = int(tag.contents[0])
    sum += num
    count += 1
print ('Count', count)
print ('Sum', sum)
