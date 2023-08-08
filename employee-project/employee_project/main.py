# importing sys
import sys

#add my folder
sys.path.insert(1, 'C:\development\python-test\employee-project\employee_project\modules')

from calculation import add

print(add(4,5))
