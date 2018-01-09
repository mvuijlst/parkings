import urllib.request, json, time

url = 'https://datatank.stad.gent/4/mobiliteit/bezettingparkingsrealtime.json'

data = urllib.request.urlopen(url).read().decode('utf8')
parkings = json.loads(data)
for parking in parkings:
  plaats = parking['address'].splitlines()[0]
  totaal = parking['parkingStatus']['totalCapacity']
  over = parking['parkingStatus']['availableCapacity']
  ts = parking['parkingStatus']['lastModifiedDate']
  
  with open('/home/adhese/mvuijlst/parkings.csv', 'a') as plog:
    plog.write(ts + ';' + plaats + ';' + str(over) + ';' + str(totaal) + '\n')
    plog.closed
