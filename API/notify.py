import csv
from datetime import datetime, date, timedelta
import getopt
import json
import pandas as pd
import requests
import sys
import urllib.parse

debug = 1

sys.path.append('/home/nysomh/prod')
import mimail

argList = sys.argv[1:]
if len(argList) < 1:
  print("Args required")
  exit(9)

options = "he:"

try:
  args, vals = getopt.getopt(argList, options)
  for thisarg, thisval in args:
    if debug > 1:
        print("arg,val:",thisarg,thisval)
    if thisarg in ("-e"):
      thisevent = thisval
    elif thisarg in ("-h"):
      print(sys.argv[0],"-e redcap_event_name")
      exit()
except getopt.error as err:
  print("Invalid option", str(err))

if debug:
    print("Looking for event",thisevent)

# Set for the event to run notifications
dt=thisevent.split('_')
desc_event=dt[0].capitalize() + " " + dt[1]

#
# initialize variables
mailfrom = "planning@omh.ny.gov"
if (datetime.now().weekday() == 1): # Tuesday
    subject = "DUE TODAY: Budget Inititative Status Update"
else:
    subject = "Budget Inititative Status Update Due Soon"
basedir = '/home/nysomh/omh-budget-init/notification'
# Project specific variables
#token = 'token=A046FAE60FAA46D60141335468314BB6'
token = 'A046FAE60FAA46D60141335468314BB6'
baseline_event = 'baseline_arm_1'
baseline_e_label = 'Baseline'
baseline_inst = 'mhi_baseline'
survey_inst = 'mhi_questionnaire'
#baseaddurl = 'https://rc-1.nyspi.org/surveys/?s=WC9XRWEHANC8MRDC&'
#
url = 'https://rc-1.nyspi.org/api/'
headers = {'content-type': 'application/x-www-form-urlencoded', 'accept': 'application/json'}
logfile = basedir + '/logs/notify.log'
if debug: 
    logfile = basedir + '/logs/notify-debug.log'
today = datetime.today()

def getlink(record, event):
    data = {
        'token': token,
        'content': 'surveyLink',
        'format': 'json',
        'instrument': survey_inst,
        'event': event,
        'record': record,
        'returnFormat': 'json'
    }
    if debug > 1:
        print ("posting",data)
    r = s.post('https://rc-1.nyspi.org/api/',data=data)
    if str(r.status_code)  == '200':
        return r.text
    else:
        print("Failed to find link for",record,event)
        return "FAILED"

# get completed day_1 records 
#payload = 'token='+token+'&content=record&format=json&type=flat&filterLogic=['+baseline_event+']['+baseline_inst+'_complete] = 2 and [' + thisevent + '][' + survey_inst + '_complete] <> 2' 
# Need to pull with labels for dropdown name field
payload = 'token='+token+'&content=record&format=json&rawOrLabel=label&type=flat&filterLogic=['+baseline_event+']['+baseline_inst+'_complete] = 2 and [' + thisevent + '][' + survey_inst + '_complete] <> 2'

s = requests.Session()
r = s.post(url, data=payload, headers=headers)
if r.status_code != 200:
    print('Initial Request completed:',r.status_code)
    print(payload)
    exit()

# Pull results into dataframe
df = pd.DataFrame.from_records(r.json())
if (not df.size):
    print("No results from record search.\n",payload)
    exit()

if debug > 1:
    print("DF before filter\n",df)
df=df[df['redcap_event_name'] == baseline_e_label] # drop current month since we need the protocol data in the baseline
if debug > 1:
    print("Record pull df\n",df)

log = open(logfile, 'a', )
logger = csv.writer(log)

# CUSTOMIZE FOR PROJECT MESSAGE
body1 = "Biweekly status reporting supports agency progress on OMH's 2023 budget initiatives. Updates are due biweekly at 4 PM Mondays. You have been identified as a contact for the below items. Please click each initiative below to provide your update."
body3 = "\n\nPlease direct any questions to Erica VanDeWal at planning@omh.ny.gov.\n"
bodydebug = ""

# CUSTOMIZE FOR THE PROJECT FIELDS
for email in df.email.unique():
    if len(email) < 5:  # eliminate odd and null values
        continue
    mailto = email
    if debug:
        origmailto=mailto
        mailto = "chris.stanley@omh.ny.gov" # pull from dictionary
        bodydebug = "Message to be sent to " + email + "\n\n" 

    dfnotify=df[df['email']==email]
    body=""
    bodylink=""
    for index, row in dfnotify.iterrows():
        record = row['record_id']
        logger.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'),record,email])
# Make sure this is pulling from the basline (october) record so don't get nulls
        if row['redcap_event_name'] == baseline_e_label:
            init_name = row['mh_initiative_name_number']
            bodylink=bodylink + "\n" + "Initiative " + init_name + ":\n" + getlink(record,thisevent) # get link once, so putting in this event since it will always exist

        body = bodydebug + body1 + bodylink + body3
    
    if debug:
        print("Would send",subject,body)
        mimail.sendmsg(subject,body,mailfrom,mailto)
        a=1
#            exit()
    else:
        #print("DEBUG HAS MAIL TURNED OFF")
        mimail.sendmsg(subject,body,mailfrom,mailto)

log.close()
