
#!/usr/bin/env python
import requests
import pandas as pd
my_field = 'pci_request'
data = {
    'token': '21678CA785CE821AADC6587B07643466',
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'fields[0]': my_field,
    'fields[1]': 'record_id',
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

df = pd.DataFrame.from_records(r.json())
df2=df.filter(items=[my_field])

rslt_df = df.loc[df[my_field] == '999']
print(df)
print(df2)
print(rslt_df)
#df = pd.DataFrame.from_records(r.json())
#print(df)
