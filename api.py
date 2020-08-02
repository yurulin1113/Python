import urllib.request
import json
import ssl

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-37E19AF1-B77D-4BB4-AC94-881D5172A163&format=JSON&startTime='

context = ssl._create_unverified_context()

with urllib.request.urlopen(url, context=context) as jsondata:
    data = json.loads(jsondata.read().decode())


data1 = data['records']['location']


for d in data1:
    print(d["locationName"])
