#!/usr/bin/env python
import requests
data = {
    'token': '21678CA785CE821AADC6587B07643466',
    'content': 'record',
    'action': 'export',
    'format': 'csv',
    'type': 'flat',
    'csvDelimiter': '',
    'records[0]': '7',
    'fields[0]': 'ladder_regions',
    'fields[1]': 'ladder_imagemap',
    'fields[2]': 'macarthur_scale_complete',
    'forms[0]': 'macarthur_scale',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
print('HTTP Status: ' + str(r.status_code))
print(r.text)
