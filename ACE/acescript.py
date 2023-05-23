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

#r.json is class 'method'
print(type(r.json))

#convert my class method to json object
