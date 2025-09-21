import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

# geoload.py is the restartable spider part of process

# https://py4e-data.dr-chuck.net/opengeo?q=Ann+Arbor%2C+MI
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

#Create a simple table (Locations) with input and Raw Data for geocoding
cur.execute('''CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
nofound = 0
for line in fh:
    #Limiting API access to avoid performance issues
    if count > 100:
        print('Retrieved 100 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    #Checking if the address was already retrieved
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",(memoryview(address.encode()), ))

    #Retrieving the record, if it's not present we continue zooming in the fh file
    try:
        data = cur.fetchone()[0]
        print("Found in database", address)
        continue
    except:
        pass

    #Creating the URL (encoded needed)
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    #Opening the URL
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    #Decoding UTF-8 to Unicode (Python internal format)
    data = uh.read().decode()
    #print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    print('Retrieved', len(data), 'characters')
    count = count + 1

    #Trying to parse data
    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    #Sanity checks to verify if we are working with real data
    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        nofound = nofound + 1

    #Insert the data in data base (Locations table)
    cur.execute('''INSERT INTO Locations (address, geodata) VALUES ( ?, ? )''',(memoryview(address.encode()), memoryview(data.encode()) ) )

    conn.commit()

    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

if nofound > 0:
    print('Number of features for which the location could not be found:', nofound)

print("Run geodump.py to read the data from the database so you can visualize it on a map.")

