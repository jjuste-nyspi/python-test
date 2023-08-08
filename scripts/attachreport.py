#!/usr/bin/env python
import pandas
import requests
import openpyxl

token = '597A2BEA1947B2364EDF32793E781B92'
data = {
    'token': token,
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'fields[0]': 'record_id',
    'forms[0]': 'mhi_questionnaire',
    'events[0]': '20230724_arm_1',
    'rawOrLabel': 'label',
    'rawOrLabelHeaders': 'label',
    'exportCheckboxLabel': 'true',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
print('HTTP Status: ' + str(r.status_code))

# generate dataframe
df = pandas.DataFrame(r.json())

# generate report

# select the columns
df2 = df.filter(['record_id','calc_duedate','status','progress_high_level_accomp','risks_concerns','questions_decisions','no_rfp___1','num_of_rfp', 'no_contracts___1', 'num_of_con_issued','no_program___1','num_of_prog_started','no_amendments___1','state_plan_amend','no_regs___1','new_rev_regs'], axis=1)

# rename the columns
df2.rename(columns={'record_id':'Initiative Number','calc_duedate': 'Previous Initiative Date', 'status':'Status','progress_high_level_accomp':'High Level Progress', 'risks_concerns':'Risks & Concerns','questions_decisions':'Questions or decisions','no_rfp___1':'Number of RFP Issued to date','num_of_rfp':'Number of RFP','no_contracts___1': 'Number of contracts issued/State Aid Letter Payments', 'num_of_con_issued':'Number of contracts','no_program___1':'Programs started','num_of_prog_started':'Number of programs','no_amendments___1':'State Plan Amendments','state_plan_amend':'Amendment Status','no_regs___1':'New Regulations','new_rev_regs':'Regulation Status'}, inplace=True)

# generate report to attach
df2.to_excel('previous-submission.xlsx', index=False)
