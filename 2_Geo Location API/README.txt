Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/opengeo.py. The program
will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve
the first plus_code from the JSON. An Open Location Code (https://en.wikipedia.org/wiki/Open_Location_Code) is a textual
identifier that is another form of address based on the location of the address.


API End Points
To complete this assignment, you should use this API endpoint that has a static subset of the Open Street Map Data.

http://py4e-data.dr-chuck.net/opengeo?
This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get
"No address..." response.
To call the API, you need to provide the address that you are requesting as the q= parameter that is properly URL encoded
using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/opengeo.py


Test Data / Sample Execution
You can test to see if your program is working with a location of "South Federal University" which will have a plus_code
of "6FV8QPRJ+VQ".

$ python solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 1505 characters
Plus code 6FV8QPRJ+VQ
Turn In

Please run your program to find the plus_code for this location:
IT College of Estonia

ANSWER: Plus code 9FFW82PW+VV
Make sure to enter the name and case exactly as above and enter the plus_code and your Python code below. Hint: The first
five characters of the plus_code are "9FFW8 ..."
Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work with
the Google API - but the plus_code may not match for this assignment.