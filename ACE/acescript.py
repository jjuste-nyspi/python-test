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
    'records[0]': '3',
    'fields[0]': 'record_id',
    'fields[1]': 'prog_id',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
print('HTTP Status: ' + str(r.status_code))
# print(r.json())

#pull record id value

df = pd.DataFrame.from_records(r.json())

df['prog_id'] = 'PRG_' + df['record_id'] + df['prog_id'].astype(str)

print(df)


#if prog_id is null, append record id to string prefix

#insert new prog id into json object


#import to redcap
