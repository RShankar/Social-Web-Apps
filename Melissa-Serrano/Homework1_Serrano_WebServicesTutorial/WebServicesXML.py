import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'  #Google Maps API URL used to search for geocode information

while True:
    address = raw_input('Enter location: ')  #get a location from the user
    if len(address) < 1 : break  #get out (since no address was entered) and ask the user to Enter Location again

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})  #Append the location entered by the user to the Google Maps API URL
    print 'Retrieving', url
    uh = urllib.urlopen(url)  #library function used to open the URL
    data = uh.read()  #location data retrieved by API
    print 'Retrieved',len(data),'characters'  #character count for data retrieved
    print data  #No problem printing the XML String
    print 'type(data) = ', type(data)
    tree = ET.fromstring(data)  #fromstring(parameter) converts the string representation of the XML into a 'tree' of XML nodes


    results = tree.findall('result')  #findall(parameter) retrieves a Python list of sub-trees that represent structures in the XML tree
    lat = results[0].find('geometry').find('location').find('lat').text  #set latitude
    lng = results[0].find('geometry').find('location').find('lng').text  #set longitude
    print 'lat',lat,'lng',lng
    location = results[0].find('formatted_address').text
    print location
	
    
    #traverse the subtree to get the country code
    addresses = tree.findall('result/address_component')
    try: 
	for item in addresses:
	    if(item.find('type').text == 'country'):
		country_code = item.find('short_name').text  #get the 2 character country code
	    else:
		country_code = None
    except: country_code = None
    print 'Country Code: ', country_code