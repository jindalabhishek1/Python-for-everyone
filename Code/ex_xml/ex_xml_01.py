# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_888987.xml (Sum ends with 78)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import sys

url = input('Enter location: ')
try:
    print('Retrieving', url)
    html = urllib.request.urlopen(url).read()
except:
    print('Retrieving failed')
    sys.exit()
print ('Retrieved', len(html), 'characters')
tree = ET.fromstring(html)

lst = tree.findall('.//count')

count = 0
sum = 0
for item in lst:
    sum += int(item.text)
    count += 1

print ('Count:', count)
print ('Sum', sum)
