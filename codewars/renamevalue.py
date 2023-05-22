#!/usr/bin/env python
import requests
import json
import pandas as pd

data = {
    'token': '9E26D0A9801C4895B340D22CD6B6196B',
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
print(r.json())

#get my data
df = pd.DataFrame.from_records(r.json())
#df['record_id'] = pd.RangeIndex(stop=df.shape[0])
df['record_id'] = ['str_%s' %i for i in range(1, len(df) + 1)]
#df['record_id'] = range(1, 1+len(df))
print(df)

#dictionary = r.json()

#json_object = json.dumps(dictionary, indent=4)


#update my data



#send results to text file

#with open("results.json", "w") as outfile:
   # outfile.write(json_object)