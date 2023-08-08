class Person:
    def __init__(self, name):
        self.name = name
  
    def talk(self):
        print(f"Hello {self.name}")


person1 = Person("Jim Smith")
person1.talk()