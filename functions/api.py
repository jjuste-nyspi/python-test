import requests
response_API = requests.get('https://gmail.googleapis.com/$discovery/rest?version=v1')
print(response_API.status_code)