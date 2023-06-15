#!/usr/bin/env python
import pandas as pd
import requests
import xlwt
import pandas


#export data
token = '597A2BEA1947B2364EDF32793E781B92'
current_event = '20230529_arm_1'

data = {
    'token': '597A2BEA1947B2364EDF32793E781B92',
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'events[0]': current_event,
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

df = pd.DataFrame(r.json())

#drop columns
df = df.drop(columns=['redcap_event_name','text'])



#remove pandas indexed column

# rename row headers

#insert na in certain columns

#erase any necessary columns


print(df)



#output excel file
output = df.to_excel('output.xlsx')