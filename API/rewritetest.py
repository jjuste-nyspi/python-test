#!/usr/bin/env python
import requests
import pandas as pd

data = {
    'token': '21678CA785CE821AADC6587B07643466',
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'fields[0]': 'record_id',
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

df = pd.DataFrame(r.json())

data = {
    'token': '21678CA785CE821AADC6587B07643466',
    'content': 'generateNextRecordName'
}
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
print('HTTP Status: ' + str(r.status_code))
print(r.text)

df = pd.DataFrame([r.text], columns=['record_id'])
print(df)

newid = r.text





