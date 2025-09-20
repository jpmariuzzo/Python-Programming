import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

# XPath selector string to look through the entire tree of XML for any tag named 'count'
counts = tree.findall('.//count')
nums = list()
for result in counts:
    nums.append(int(result.text))

print('Count:', len(nums))
print('Sum:', sum(nums))
