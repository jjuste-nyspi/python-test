class Employee(object):
    # count employees
    empcount = 0

    # attributes
    def __init__(self, name, job_title, department, salary, hire_year):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year
        Employee.empcount =+ 1
    
    def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

    # returns string representation
    def __str__(self):
        result = f'String Representation: Name: {self.name}, Job Title: {self.job_title}, Department: {self.department}, Salary: {self.salary}, Hire Year: {self.hire_year}'
        return result
    # returns years_worked
    def years_worked(self, hire_year, current_year):
        result = current_year - self.hire_year
        return result

