class Employee(object):
    def __init__(self, name, age, job_title, department, salary, hire_year):
        self.name = name
        self.age = age
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

    def set_age(self, age):
        self.age = age

    def get_age(self,age):
        return self.age
    def __str__(self):
        return f"{self.name}, {self.age}, {self.job_title}, {self.department}, {self.salary}, {self.hire_year}"

e1 = Employee("Jean", 38, "developer", "redcap", 30000, 2022)
e1.set_age(45)
print(e1)