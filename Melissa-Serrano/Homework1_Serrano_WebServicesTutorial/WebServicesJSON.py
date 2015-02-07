import urllib
import json  

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'  #Google Maps API URL used to search for geocode information

while True:
    address = raw_input('Enter location: ')  #get a location from the user
    if len(address) < 1 : break  #get out (since no address was entered) and ask the user to Enter Location again

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})  #Append the location entered by the user to the Google Maps API URL
    print 'Retrieving', url
    uh = urllib.urlopen(url) #library function used to open the URL
    data = uh.read()  #location data retrieved by API
    print 'Retrieved',len(data),'characters'  #character count for data retrieved 
    try: js = json.loads(str(data))  #json.loads(parameter) takes a JSON string and gives us a Python Dictionary so we can traverse the data
    #retrieved or use square bracket notation to access elements
    except: js = None  #if there's a problem setting js then set it to None (Null)
    if 'status' not in js or js['status'] != 'OK':  #When the data is retrieved successfully there is a key-value pair status:OK
        print '==== Failure To Retrieve ===='
        print data
        continue

    print json.dumps(js, indent=4)  #json.dumps will take a Python object (usually Dictionary) and serialize it to JSON
    print 'type(js) = ', type(js)
	
    lat = js["results"][0]["geometry"]["location"]["lat"]  #store the latitude
    lng = js["results"][0]["geometry"]["location"]["lng"]  #store the longitude
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location
    
    #js["results"][0]["address_components"][N]
    #where N = 0 is the Locality address component
          #N = 1 is the State address component
          #N = 2 is the Country address component
    
    #Now we can use the Python Dictionary Format to access the data we need
    try: country_code = js["results"][0]["address_components"][3]["short_name"]  #get the 2 character country code
    except: country_code = None
   
    print 'Country Code: ', country_code
    
    