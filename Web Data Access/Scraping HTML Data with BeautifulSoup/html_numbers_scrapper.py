import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_2070616.html'
#url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

#Retrieve all of the anchor tags
tags = soup('span')

c = 0
add = 0
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    c = c + 1
    add = add + int(tag.contents[0])
print('Count ', c)
print('Sum ', add)
