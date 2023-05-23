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

# check if record id format is correct

#print(df)


#test = df["record_id"].str.contains('z').any()

#print(test)

# if column has proper prefix, skip, otherwise append prefix and leading zeroes

mask = df[['record_id']].apply(lambda x: x.str.contains('P',regex=False)).any(axis=1)
print(df[mask])

# leading zeroes
#df["record_id"] = df["record_id"].map(lambda x: f'{x:0>5}')
# append prefix
#df["record_id"] = 'PRG_1' + df["record_id"].astype(str)

#print(df["record_id"])
df['column_is_digit'] = list(map(lambda x: x.isdigit(), df['record_id']))

#update record id with prefix and leading zeroes

#rename record(s)

#identify record id's that do not fit a pattern via regex

#find the next free number

#rename record
