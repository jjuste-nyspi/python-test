first = 'John'
last = 'Smith'
message = first + ' [' + last + '] ' + 'is a coder.'
msg = f'{first} [{last}] is a coder'
print(msg)

course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(len(course))

x = 10
x += 3
print(x)

def mul_by_n(lst, n):
    print("Inputs: ", lst, n) # Check our inputs
    result = (x * n for x in lst)
    print("Result: ", list(result)) # Check our result
    return list(result)

mul_by_n([1, 2, 3], 4)