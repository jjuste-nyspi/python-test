#!/usr/bin/env python
import requests
data = {
    'token': 'B5A899A8421A1C734580CEC4A8146108',
    'content': 'project',
    'format': 'json',
    'returnFormat': 'json'
}
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
print('HTTP Status: ' + str(r.status_code))
print(r.json())
