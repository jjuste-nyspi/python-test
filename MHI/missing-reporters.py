#!/usr/bin/env python
import pandas
import requests

#baseline data
data = {
    'token': '597A2BEA1947B2364EDF32793E781B92',
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'fields[0]': 'record_id',
    'fields[1]': 'f_name',
    'fields[2]': 'l_name',
    'fields[3]': 'email',
    'events[4]': 'baseline_arm_1',
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

baseline_df = pandas.DataFrame(r.json())
#print(baseline_df)


#current data
data = {
    'token': '597A2BEA1947B2364EDF32793E781B92',
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'fields[0]': 'record_id',
    'fields[1]': 'f_name',
    'fields[2]': 'l_name',
    'fields[3]': 'email',
    'events[4]': '20230529_arm_1',
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

current_event_df = pandas.DataFrame(r.json())
#print(current_event_df)

# pull record id's from current events that responded
lst = [i for i in current_event_df['record_id']]
print(lst)


#df['available'] = df.apply(lambda row: row[row == 1].index.tolist(), axis=1)
#remove those record id's from baseline