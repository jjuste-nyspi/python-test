def string_or_num(s):
    if s.isdigit() == True:
        result = (int(s) * 50) + 6
        print(result)
    else:
        print("This is a letter")

string_or_num("5")


# x = "n"
# y = x.isdigit()
# print(y)