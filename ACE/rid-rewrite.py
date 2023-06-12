"""
ACE requires a Progress ID
The syntax is PRG_1[sequential-5-digits-with-leading-zeros] (e.g. PRG_100013).
Find the next free record ID number and rename to that pattern
"""
#!/usr/bin/env python
import requests
import pandas as pd
import re


#export
token = '9E26D0A9801C4895B340D22CD6B6196B'
data = {
    'token': token,
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
#print(r.json())

# get dataframe from response
df = pd.DataFrame(r.json())
print(df)