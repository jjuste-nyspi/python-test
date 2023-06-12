#!/usr/bin/env python
import requests
data = {
    'token': '21678CA785CE821AADC6587B07643466',
    'content': 'project',
    'format': 'json',
    'returnFormat': 'json'
}
r = requests.post('https://rc-1.nyspi.org/api/',data=data)
print('HTTP Status: ' + str(r.status_code))
print(r.json())
