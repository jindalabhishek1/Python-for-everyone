# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_888988.json (Sum ends with 64)

import json
import urllib.request, urllib.parse, urllib.error
import sys

url = input('Enter location: ')
try:
    print('Retrieving', url)
    html = urllib.request.urlopen(url).read()
except:
    print('Retrieving failed')
    sys.exit()
print ('Retrieved', len(html), 'characters')

data = html.decode()
js = json.loads(data)

count = 0
sum = 0
for comment in js['comments']:
    count += 1
    sum += comment['count']

print ('Count: ',count)
print ('Sum: ', sum)
