
"""
This script will update the next week's checkbox to match the value from the previous week
1. Get Current Arm, Record Id's and Checkbox values
2. Extract next arm name
3. Replace current arm name with next arm name
4. Import records
"""
#!/usr/bin/env python
import pandas as pd
import requests

# Get Current Arm, Record Id's and Checkbox values
token = 'D8D0F3E74F0053E53D920CDFCED50BF7'
current_event = '20230612_arm_1'
data = {
    'token': token,
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'fields[0]': 'no_rfp',
    'fields[1]': 'no_contracts',
    'fields[2]': 'no_program',
    'fields[3]': 'no_amendments',
    'fields[4]': 'no_regs',
    'fields[5]': 'record_id',
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
# print(r.json())

# my dataframe
df = pd.DataFrame(r.json())


# Extract next arm name
all_arms = ['baseline_arm_1', '20230529_arm_1', '20230612_arm_1', '20230626_arm_1', '20230710_arm_1', '20230724_arm_1',
            '20230807_arm_1', '20230821_arm_1']

# iterate through and match current arm from array, select the next one, set it as next arm
for arm in all_arms:
    if arm == current_event:
        next_arm_index = all_arms.index(current_event) + 1
        next_arm = all_arms[next_arm_index]

# append next arm to current checkbox settings and drop pandas index
updated_df = df.replace(current_event, next_arm)
final_df = updated_df[['record_id', 'redcap_event_name', 'no_rfp___1', 'no_contracts___1', 'no_program___1',
                       'no_amendments___1', 'no_regs___1']]

# generate json string from dataframe
json_string = final_df.to_json(orient='records')

# import
data = {
    'token': 'D8D0F3E74F0053E53D920CDFCED50BF7',
    'content': 'record',
    'action': 'import',
    'format': 'json',
    'type': 'flat',
    'overwriteBehavior': 'normal',
    'forceAutoNumber': 'false',
    'data': json_string,
    'returnContent': 'count',
    'returnFormat': 'json'
}
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
print('HTTP Status: ' + str(r.status_code))
print(r.json())

