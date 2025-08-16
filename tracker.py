import phonenumbers
from myphone import number
from phonenumbers import geocoder as phone_geocoder, carrier
from opencage.geocoder import OpenCageGeocode

pepnumber = phonenumbers.parse(number)

location = phone_geocoder.description_for_number(pepnumber, "en")
service_provider = carrier.name_for_number(pepnumber, "en")

print("Location:", location)
print("Carrier:", service_provider)

key = "33fb79d5cd684c4f8905c20fb924c687"
oc_geocoder = OpenCageGeocode(key)

results = oc_geocoder.geocode(location)

if results:
    latitude = results[0]["geometry"]["lat"]
    longitude = results[0]["geometry"]["lng"]
    print("Latitude:", latitude)
    print("Longitude:", longitude)

    
    maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    print(" Google Maps:", maps_link)
else:
    print(" No coordinates found for this location.")
