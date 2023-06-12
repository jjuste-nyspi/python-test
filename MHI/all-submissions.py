#!/usr/bin/env python
import pandas
import requests
import xlwt

data = {
    'token': '597A2BEA1947B2364EDF32793E781B92',
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'fields[0]': 'record_id',
    'forms[0]': 'mhi_baseline',
    'forms[1]': 'mhi_questionnaire',
    'events[0]': '20230529_arm_1',
    'rawOrLabel': 'label',
    'rawOrLabelHeaders': 'label',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
print('HTTP Status: ' + str(r.status_code))
print(r.json())

df = pandas.DataFrame(r.json())
reportdf = df[['record_id','status','progress_high_level_accomp','risks_concerns','questions_decisions']]
print(df)

print(reportdf.to_excel('test.xlsx'))

