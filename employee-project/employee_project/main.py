import sys
sys.path.insert(1, 'C:\development\python-test\employee-project\employee_project\modules')

from employee import Employee

employee1 = Employee("jean", "developer", "redcap", 50000, 2022)

#string representation
#print(str(employee1))


print ("Total Employee %d" % Employee.empcount)