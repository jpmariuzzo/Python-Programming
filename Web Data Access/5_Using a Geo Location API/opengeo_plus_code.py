import urllib.request, urllib.parse
import http, json, ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)

#Making Socket/HTTP calls
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data),'characters')

#Testing data object opening
    try:
        js = json.loads(data)
    except:
        js = None

#Testing js content
    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break
#Testing content of list features
    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    plus_code = js['features'][0]['properties']['plus_code']
    print('Plus code', plus_code)