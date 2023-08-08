class Employee(object):
    def __init__(self, name, job_title, department, salary, hire_year):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year
    
    def __str__(self):
        result = f'String Representation: {self.name}'
        return result
    
    