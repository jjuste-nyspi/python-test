"""
calculate the appropriate task condition based on frequency
attempt counterbalance within group (control vs IGR positive) as identified by [yn_igr_group]

Instrument values:
eye_tracking_acquisition - int 1 through 8
eeg_acquisition - VEP/Face
oae_acquisition - Left/Right
pci - Toy/no toy - For 3-6 month visits, all PCI should be done with toy first
For all other timepoints, check to see which condition should be performed first.

Trigger from active message:
1) determine which instrument (or do as separate queues?)
2) pull [yn_igr_group] and instrument-specific value for all records
3) determine the least frequency; randomize on tie
4) write value to that record
"""

# !/usr/bin/env python
import requests
import json

# task order field on pci instrument toy/no toy
instfield = 'pci_order'

# my token, moved out of data object
token = '9E26D0A9801C4895B340D22CD6B6196B'

#our data object will query the url for these parameters
data = {
    'token': token,
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    #'fields[0]': 'yn_igr_group',
    #'fields[1]': instfield,
    'fields[2]': 'record_id',
    'fields[0]':'pci_request',
    'fields[1]': 'pci_order',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json',
    'filterLogic': "[record_id]='PRG_100030'"
}

#we make our request
r = requests.post('https://rc-1.nyspi.org/api/', data=data)
#our response via status code
print('HTTP Status: ' + str(r.status_code))

#our json response
#print(r.json())

print (type(r.json))


my_list = r.json()

print(my_list)
print(type(my_list))

# function to find pci_request = 1




