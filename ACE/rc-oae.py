"""
calculate the appropriate task condition based on frequency
attempt counterbalance within group (control vs IGR positive) as identified by [yn_igr_group]

Instrument values:
eye_tracking_acquisition - int 1 thru 8
eeg_acquisition - VEP/Face
oae_acquisition - Left/Right
pci - Toy/no toy - For 3-6 month visits, all PCI should be done with toy first
For all other timepoints, check to see which condition should be performed first.

Trigger from active message:
1) determine which instrument (or do as seperate queues?)
2) pull [yn_igr_group] and instrument-specific value for all records
3) determine least frequency; randomize on tie
4) write value to that record
"""

import json
import pandas as pd
import requests
import random


def lambda_handler(event, context):
    # function specifics
    debug = 1
    instfield = 'oae_order'
    allowed = ['Left', 'Right']
    # Pull details from the message
    body = event['Records'][0]['body']
    rid = (body.split('&record=')[1]).split('&')[0]
    instrument = (body.split('&instrument=')[1]).split('&')[0]
    rcevent = (body.split('&redcap_event_name=')[1]).split('&')[0]
    # static vars
    code = 200
    msg = 'Nothing to do'
    choice = ''
    token = 'FE0302CC85648BEE1ADD62B0C400A212'
    # get to work
    # pull critical values from REDCap
    data = {
        'token': token,
        'content': 'record',
        'action': 'export',
        'format': 'json',
        'type': 'flat',
        'csvDelimiter': '',
        'fields[0]': 'yn_igr_group',
        'fields[1]': instfield,
        'fields[2]': 'record_id',
        'rawOrLabel': 'raw',
        'rawOrLabelHeaders': 'raw',
        'exportCheckboxLabel': 'false',
        'exportSurveyFields': 'false',
        'exportDataAccessGroups': 'false',
        'returnFormat': 'json',
        'filterLogic': '[enrollment_and_consent_complete]=2'
    }
    r = requests.post('https://rc-1.nyspi.org/api/', data=data)
    if r.status_code != 200:
        print('Post Failed - HTTP Status: ' + str(r.status_code))
        msg = "Failed Post"
        code = 500
        return {
            'statusCode': code,
            'body': json.dumps(msg)
        }

    # get frequency among all possible values (even if not currently assigned)
    df = pd.DataFrame.from_records(r.json())
    if debug:
        print(df)
    # Need frequency by IGR GROUP so drop the opposite
    thisgroup = df.loc[df['record_id'] == rid, 'yn_igr_group'].unique()[0]
    if debug:
        print(type(thisgroup))
        print("This group is", thisgroup)
    df = df[df['yn_igr_group'] == thisgroup]

    df1 = df[instfield].value_counts()
    if debug:
        print("df1\n", df1)
    active = df[instfield].tolist()
    if debug:
        print("active\n", active)
    missing = list(set(allowed).difference(active))
    if len(missing):
        choice = random.choice(missing)
        print("I pick missing", choice)
    else:
        dfct = df[instfield].value_counts()
        if debug:
            print("dfct\n", dfct)
        least = dfct[dfct == dfct.min()].index
        choice = random.choice(least)
        print("I pick active", choice)

    # Prepare and send update to REDCap
    record = {
        'record_id': rid,
        'redcap_event_name': rcevent,
        instfield: choice,
        instrument + '_complete': '1'
    }

    recjson = json.dumps([record])

    data = {
        'token': 'FE0302CC85648BEE1ADD62B0C400A212',
        'content': 'record',
        'action': 'import',
        'format': 'json',
        'type': 'flat',
        'overwriteBehavior': 'normal',
        'forceAutoNumber': 'false',
        'data': recjson,
        'returnContent': 'count',
        'returnFormat': 'json'
    }
    r = requests.post('https://rc-1.nyspi.org/api/', data=data)
    if r.status_code != 200:
        msg = 'META get HTTP Status: ' + str(r.status_code)
        code = 500
        return {
            'statusCode': code,
            'body': json.dumps(msg)
        }
    return {
        'statusCode': code,
        'body': json.dumps(msg)
    }
