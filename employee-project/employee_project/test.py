class Student:
    NUM_GRADES = 5

    def __init__(self, name):
        self.name = name
        self.grades = []
        for i in range(Student.NUM_GRADES):
            self.grades.append(0)

    def __str__(self):

        result = f'this is string representation {self.name }'
        return result
    
s1 = Student('Mary')
print(s1)
s2 = Student('Bill')
print (str(s1) + '\n' + str(s2))
