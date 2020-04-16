from mygeotab import API, dates
import json
from datetime import date, timedelta
import sys
import simplekml
from config import *



if len(sys.argv) == 5:
    #start the connection
    client = API(username=username, password=password, database=database)
    client.authenticate()
    kml=simplekml.Kml()
    year=int(sys.argv[1])
    month=int(sys.argv[2])
    day=int(sys.argv[3])
    input_date = date(year, month, day)
    vehicle=str(sys.argv[4])
    device_id=client.get('Device', name=vehicle)[0]['id']
    filename=str(year)+"-"+str(month)+"-"+str(day)+"_"+vehicle
    fromdate=input_date.strftime("%Y-%m-%d")+"T00:00:00.000Z"
    todate=(input_date+timedelta(days=1)).strftime("%Y-%m-%d")+"T00:00:00.000Z"
    query = client.get("LogRecord", search = {"fromDate": fromdate,"toDate": todate,"deviceSearch":{"id":device_id}})
    for row in query:
        kml.newpoint(name=str(row['dateTime']), coords=[(str(row['longitude']),str(row['latitude']))], description='speed:'+str(row['speed'])+"km/h")
    kml.save(filename+'.kml')

if len(sys.argv) < 5:
    print('Extract the trip of a day in kml format')
    print("Usage:",sys.argv[0]," Year Month Day vehicle-code")
