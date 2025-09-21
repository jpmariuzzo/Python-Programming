import urllib.request, urllib.parse
import http, json, ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the URL to file: ')



url = url.strip()
jshand = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(jshand), 'characters...')
try:
    js = json.loads(jshand)
except:
    js = None

lst = list()

for item in js['comments']:
    lst.append(int(item['count']))
print('Items:', len(js['comments']))
print('Sum:', sum(lst))





