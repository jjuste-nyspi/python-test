#!/usr/bin/env python
import requests
import json
import pandas as pd

data = {
    'token': '5F65D219291AFD9F51F5279EA557D2B6',
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'eav',
    'csvDelimiter': '',
    'fields[0]': 'yn_igr_group',
    'fields[1]': 'pci_request',
    'fields[2]': 'pci_order',
    'events[0]': 'month6_arm_1',
    'events[1]': 'month9_arm_1',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json',
    'filterLogic': '[enrollment_and_consent_complete]=2'
}

r = requests.post('https://rc-1.nyspi.org/api/',data=data)
print('HTTP Status: ' + str(r.status_code))
print(r.json())

#get my data
df = pd.DataFrame.from_records(r.json())
df['record'] = ['PRG_%s' %i for i in range(1, len(df) + 1)]
print(df)

#dictionary = r.json()

#json_object = json.dumps(dictionary, indent=4)


#update my data



#send results to text file

#with open("results.json", "w") as outfile:
   # outfile.write(json_object)