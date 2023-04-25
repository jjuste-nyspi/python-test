from redcap import Project

api_url = 'https://rc-1.nyspi.org/api/'
api_key = '21678CA785CE821AADC6587B07643466'
project = Project('https://rc-1.nyspi.org/api/', '21678CA785CE821AADC6587B07643466')

data = project.export_records()
print(data)