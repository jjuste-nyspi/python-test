import redcap
from redcap import Project

api_url = 'https://rc-1.nyspi.org/api/'
api_key = '21678CA785CE821AADC6587B07643466'
project = Project('https://rc-1.nyspi.org/api/', '21678CA785CE821AADC6587B07643466')

new_records = [
    {'record_id': '7', 'pat_first_name': 'Mr', 'pat_last_name': 'Red', 'patient_information_complete': '2'}
]

project.import_records(new_records)
project.delete_records(["3"])


