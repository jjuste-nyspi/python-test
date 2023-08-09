# grocery list class declaration with list of dictionaries for grocery list
class GroceryList:
# init method, will default to empty allowing user to add one item at a time
    def __init__(self, dictionary):
        self.name = None
        self.quantity = None
        self.price = None
        # user can also pass in list of dictionaries to initiatlize grocery list
        # create class instance from dictionary
        for key, value in dictionary.items():
            setattr(self, key, value)

my_dict = {'name': 'grapefruit','quantity': 3, 'price': 2.00}

# dictionary items
print(my_dict.items())

# methods

    #string representation

    #add item

    #remove item

    #update price

    #update quantity

    #get list

    #get total cost

    #save list



#create main.py and import into new file
#create a function read list that accepts file, opens and creates dictionaries

#brings in dictionary

class Employee(object):
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
d = {'name': 'Oscar', 'last_name': 'Reyes', 'age':32 }
e = Employee(**d) 
print (e.name) # Oscar 
print (e.age + 10) # 42 


#initialize with dictionary
class Developer():
    def __init__(self, dictionary):
        self.name = None
        self.salary = None
        self.language = None

        for key, value in dictionary.items():
            setattr(self, str(key).replace(' ', '_'), value)


my_dict = {'first name': 'bobbyhadz', 'salary': 50, 'language': 'Python'}

bob = Developer(my_dict)

print(bob.name)  # 👉️ bobbyhadz
print(bob.salary)  # 👉️ 50
print(bob.language)  # 👉️ Python