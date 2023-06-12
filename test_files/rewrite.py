#!/usr/bin/env python
import requests
import pandas as pd

token = '21678CA785CE821AADC6587B07643466'

data = {
    'token': token,
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
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
print(df)

