def to_underscore(string):

    #test string

    #if string is a type of int, convert and return as a string
    if (type(string)) == int:
        convertednum = str(string)
        print(type(convertednum))
    elif (type(string)) == str:
        newString = string.isupper()
        print(newString)
        print("I am a string")


    #if string is letters, find the capital letters and insert an underscore, than convert all to lowercase and return result



to_underscore("TestController")
to_underscore("MoviesAndBooks")
to_underscore("App7Test")
to_underscore(1)