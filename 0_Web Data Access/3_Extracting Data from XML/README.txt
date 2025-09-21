Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/xml3.py. The program
will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from
the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other
is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_2070618.xml (Sum ends with 11)
You do not need to save these files to your folder since your program will read the data directly from the URL.
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
Data Format and Approach
The data consists of a number of names and comment counts in XML as follows:

<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>
You are to look through all the <comment> tags and find the <count> values sum the numbers. The closest sample code that
shows how to parse XML is xml3.py.
To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any
tag named 'count' with the following line of code:

counts = tree.findall('.//count')
Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also
work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.
Sample Execution


$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
Retrieved 4189 characters
Count: 50
Sum: 2...


################## EXAMPLE ### xml3.py #######################

import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    # Debug print the data :)
    print(result.text)

print('Count:', len(nums))
print('Sum:', sum(nums))

##############################################################