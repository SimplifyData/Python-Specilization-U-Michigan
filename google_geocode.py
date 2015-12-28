import urllib.parse as urlparse
import  urllib.request as urlreq

import json

def geocode_address(service_url):
    """
    this function corrects the writen address, by checking it from json api and google geocode api.
    json is used for parsing and encoding the correct url for google api.
     urllib is used for connect to the url.
    :return:
    """
    while True:
        try:

                address = input("Enter your address: ")

                if len(address) < 1 : break

                url = service_url + urlparse.urlencode({'sensor':'false', 'address': address})

                print('Retrieving: ', url)

                data = urlreq.urlopen(url).read()

                print('Retrieved ', len(data), ' characters')

        except:
            print("Enter a valid address")

        try:
            result = json.loads(data.decode("utf-8"))

        except:

            result = None

            print("There is no data in the file")

            print(data)

        if 'status' not in result or result['status'] != 'OK':
            print('===Failure to Retrieve===')

            print(data)

            continue

        print (json.dumps(result, indent= 4))

        place_id = result["results"][0]["place_id"]

        return place_id

service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

geocode_app = geocode_address(service_url)

print(geocode_app)











