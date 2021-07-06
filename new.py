#!/usr/bin/python3

import cgi
import subprocess
import requests
import xmltodict
import json

print("content-type: text/html")
print()

f = cgi.FieldStorage()

plate_no = f.getvalue("x")
r = requests.get("http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={}&username=YOURUSERNAME".format(plate_no))

data = xmltodict.parse(r.content)
jdata = json.dumps(data)
df = json.loads(jdata)
df1 = json.loads(df['Vehicle']['vehicleJson'])
print("Description     : ",df1["Description"])
print("RegistrationDate: ",df1["RegistrationDate"])
print("Location        : ",df1["Location"])
print("NumberOfSeats   : ",df1["NumberOfSeats"]["CurrentTextValue"])
print("VehicleIdentificationNumber: ",df1["VechileIdentificationNumber"])
print("EngineNumber    : ",df1["EngineNumber"])
print("EngineSize      : ",df1["EngineSize"]["CurrentTextValue"])
print("FuelType        : ",df1["FuelType"]["CurrentTextValue"])




