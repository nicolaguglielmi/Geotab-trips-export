import asyncio
from mygeotab import API, dates
import json
import csv
from datetime import date, timedelta
import os
from config import *

#create folder for containing results
if not os.path.exists('data'):
    os.makedirs('data')

devices=[]
client = API(username=username, password=password, database=database)
client.authenticate()

#find all devices visible to the service account
device = client.call('Get', typeName='Device')
for j in device:
  devices.append([j['name'],j['id']])

#iterate over the data range
while start_date <= end_date:
  fromdate=start_date.strftime("%Y-%m-%d")+"T00:00:00.000Z"
  todate=(start_date+data_range).strftime("%Y-%m-%d")+"T00:00:00.000Z"
  for dev in devices:
    result=[]
    filename=start_date.strftime("%Y-%m-%d")+"-"+dev[0]
    query = client.get("LogRecord", search = {"fromDate": fromdate,"toDate": todate,"deviceSearch":{"id":dev[1]}})
    for row in query:
      if int(row['speed'])>0:
        result.append([row['latitude'],row['longitude'],row['speed']])
    if len(result)>0:
      csv=open("data/"+filename+".csv",'w+')
      csv.write('Latitude,Longitude,Speed\n')
      for j in result:
        csv.write(str(j[0])+","+str(j[1])+","+str(j[2])+'\n')
      csv.close()
      print(fromdate+" "+dev[0])
  start_date += data_range