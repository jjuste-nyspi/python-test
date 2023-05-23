"""
ACE requires a Progress ID
The syntax is PRG_1[sequential-5-digits-with-leading-zeros] (e.g. PRG_100013).
Find the next free record ID number and rename to that pattern
"""

#!/usr/bin/env python
import requests
import pandas as pd

data = {
    'token': '9E26D0A9801C4895B340D22CD6B6196B',
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'fields[0]': 'record_id',
    'forms[0]': 'initial_contact',
    'events[0]': 'intake_arm_1',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
#print('HTTP Status: ' + str(r.status_code))
#print(r.json())

df = pd.DataFrame(r.json())

#locate columns that need to be formatted
filtered_df = df[~df["record_id"].str.contains("PRG")]

#variable for lead zeroes
lead_zeroes_df = filtered_df

#add my lead zeroes
lead_zeroes_df["record_id"] = df["record_id"].map(lambda x: f'{x:0>5}')

#variable for prefix
append_prefix_df = lead_zeroes_df

#append my prefix
append_prefix_df["record_id"] = 'PRG_1' + lead_zeroes_df["record_id"].astype(str)

print(append_prefix_df)



