import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl


#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

i = 0
names_pos = list()
names_pos.append(str(input('Enter URL: ')))

cnt = int(input('Enter count: '))
pos = int(input('Enter position: '))

while i < cnt:
    html = urllib.request.urlopen(names_pos[i], context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    names = list()
    for tag in tags:
        names.append(tag.get('href', None))
    url = str(names[pos-1])
    names_pos.append(url)
    i = i + 1

for n in names_pos:
    print('Retrieving:', n)









