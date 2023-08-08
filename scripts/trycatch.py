def count_sheeps(sheep):
  newarray = []
  for x in sheep:
      if x == True:
          x = 1
          newarray.append(x)
          Sum = sum(newarray)
          print(Sum)

count_sheeps([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True])