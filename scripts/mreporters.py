#!/usr/bin/env python
import getopt
import pandas
import requests


# export baseline data
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
    'fields[4]': 'mh_initiative_name_number',
    'events[0]': 'baseline_arm_1',
    'rawOrLabel': 'label',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
if not str(r.status_code) == '200':
    print('HTTP Status: ' + str(r.status_code))
    exit()
#print(r.json())

# baseline variable
baseline_df = pandas.DataFrame(r.json())

thisevent = '20230724_arm_1'

# export current data event data
data = {
    'token': '597A2BEA1947B2364EDF32793E781B92',
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'fields[0]': 'record_id',
    'fields[3]': 'email',
    'events[0]': thisevent,
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
if not str(r.status_code) == '200':
    print('HTTP Status: ' + str(r.status_code))
    exit()
print(r.json())

# current event variable
current_event_df = pandas.DataFrame(r.json())

# pull record id's from current events that responded
# populate list for yes respondents
yes_respondents = [i for i in current_event_df['record_id']]

#extract these yes respondents from baseline
finaldf = baseline_df[~baseline_df['record_id'].isin(yes_respondents)]
finaldf.dropna(subset=['email'],inplace=True)
finaldf = finaldf[finaldf['email'].str.len()>3]
finaldf = finaldf[['record_id','mh_initiative_name_number','email']]
finaldf.to_excel('adfsdf.xlsx',index=False)


