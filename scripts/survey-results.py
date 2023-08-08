"""
Pull down current arm info for weekly MHI Reports. Generate excel report for further cleanup with vba script.
"""
#!/usr/bin/env python
import requests
import pandas
import xlwt

# export current report info
# my token and current event

token = '597A2BEA1947B2364EDF32793E781B92'
current_arm = '20230612_arm_1'
#!/usr/bin/env python
import requests
data = {
    'token': '597A2BEA1947B2364EDF32793E781B92',
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'fields[0]': 'record_id',
    'fields[1]': 'initiative_end_label',
    'fields[9]': 'desc_initiative',
    'fields[11]': 'status',
    'fields[12]': 'progress_high_level_accomp',
    'fields[13]': 'risks_concerns',
    'fields[14]': 'questions_decisions',
    'fields[15]': 'no_rfp',
    'fields[16]': 'num_of_rfp',
    'fields[17]': 'desc_rfp',
    'fields[18]': 'no_contracts',
    'fields[19]': 'num_of_con_issued',
    'fields[20]': 'desc_contracts',
    'fields[21]': 'no_program',
    'fields[22]': 'num_of_prog_started',
    'fields[23]': 'desc_prog',
    'fields[24]': 'no_amendments',
    'fields[25]': 'state_plan_amend',
    'fields[26]': 'desc_amendment',
    'fields[27]': 'no_regs',
    'fields[28]': 'new_rev_regs',
    'fields[29]': 'desc_regs',
    'fields[30]': 'mhi_questionnaire_complete',
    'events[0]': current_arm,
    'rawOrLabel': 'label',
    'rawOrLabelHeaders': 'label',
    'exportCheckboxLabel': 'true',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
print('HTTP Status: ' + str(r.status_code))
print(r.json())

r = requests.post('https://rc-1.nyspi.org/api/',data=data)
print('HTTP Status: ' + str(r.status_code))
# print(r.json())

df = pandas.DataFrame(r.json())

finaldf = df.to_excel('output.xlsx')









# create report





# email me report for cleanup


