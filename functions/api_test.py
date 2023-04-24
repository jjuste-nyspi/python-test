from redcap import Project

api_url = 'https://rc-1.nyspi.org/api/'
api_key = 'B5A899A8421A1C734580CEC4A8146108'
project = Project('https://rc-1.nyspi.org/api/', 'B5A899A8421A1C734580CEC4A8146108')

data = project.export_records()
project.delete_records(["20"])

print(data)