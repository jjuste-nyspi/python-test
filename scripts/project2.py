class Employee(object):
    def __init__(self, name, job_title, department, salary):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"Your name is {self.name}, you are a {self.job_title}. You work as a" \
               f" {self.department}. You earn {self.salary}"

p1 = Employee("Jean", "developer", "redcapadmin", 40000)
print(p1)