#!/usr/bin/env python
import csv
from datetime import datetime, timedelta
import requests
import pandas as pd
import sys
import warnings

event = '20230529_arm_1' # NEED TO ADD ARG OPTS

debug = 9
warnings.filterwarnings("ignore",category=pd.core.common.SettingWithCopyWarning)

basedir="/home/nysomh/omh-budget-init/link/"
proddir="/home/nysomh/prod/"
sys.path.append(proddir)
import dbcon

linkfile=basedir+"linkframe.csv"
rewritefile=basedir+"hostbed.txt"

token=dbcon.mhitoken
# Get active baseline records 
data = {
    'token': token,
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'fields[0]': 'record_id',
    'filterLogic': '[baseline_arm_1][mhi_baseline_complete]=2'
}
if debug:
    print("Requesting:\n",data)
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
if debug:
    print('HTTP Status: ' + str(r.status_code))
if (r.status_code != 200):
    print("ERROR CONNECTING TO REDCAP",str(r.status_code))
    exit(1)

# Pull results into dataframe
df = pd.DataFrame.from_records(r.json())
if (not df.size):
    print("No records. Odd")
    exit()

# Get completed survey submissions since 

# get link rewrite data
linkdf=pd.read_csv(linkfile,dtype=str)
if debug:
  print("Link frame at start\n",linkdf)

# get new link
for index,row in df.iterrows():
  record = row["record_id"]
  data = {
        'token': token,
        'content': 'surveyLink',
        'format': 'json',
        'instrument': 'mhi_questionnaire',
        'event': event,
        'record': record,
        'returnFormat': 'json'
  }
  r = requests.post('https://rc-1.nyspi.org/api/',data=data)
  #r = s.post('https://rc-1.nyspi.org/api/',data=data)
  if str(r.status_code)  == '200':
    if debug:
      print("Setting new link for record",record,"to",r.text)
#      print(linkdf['record_id'] == record)
    linkdf.loc[linkdf.record_id==record,'link'] = r.text
  else:
    print("Failed to find link for",record,event)

if debug:
  print("Updated linkdf\n",linkdf)

# write link to rewrite df
linkdf.to_csv(linkfile,index=False)
linkdf.to_csv(rewritefile,sep=' ',columns=['simple','link'],index=False,header=False)
