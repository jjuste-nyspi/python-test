#!/usr/bin/env python
import requests
import json

data = {
    'token': '21678CA785CE821AADC6587B07643466',
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'fields[0]': 'record_id',
    'fields[1]': 'fname',
    'fields[2]': 'lname',
    'fields[3]': 'patient_info_complete',
    'fields[4]': 'prog_id',
    'fields[5]': 'program_id_complete',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
print('HTTP Status: ' + str(r.status_code))
print(r.json())

# records containing null program id's
nullprogid = json.dumps(r.json())

# convert json string to json object
jsonObject = json.loads(nullprogid)
#print(jsonObject)
#print(type(jsonObject))

for obj in jsonObject:
  if obj["prog_id"] == '':
    obj["prog_id"] = 'PROG_' + obj["record_id"]

print(jsonObject)
print(type(jsonObject))


recjson = json.dumps(jsonObject)

data = {
    'token': '21678CA785CE821AADC6587B07643466',
    'content': 'record',
    'action': 'import',
    'format': 'json',
    'type': 'flat',
    'overwriteBehavior': 'normal',
    'forceAutoNumber': 'false',
    'data': recjson,
    'returnContent': 'count',
    'returnFormat': 'json'
}
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
print('HTTP Status: ' + str(r.status_code))
print(r.json())






