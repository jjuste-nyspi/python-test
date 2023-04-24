weight = int(input("Weight: "))
kilorlbs = input("(K)g or (L)bs: ")
if kilorlbs == 'L' or 'l':
    result = weight * .4535
    print("You weight " + str(result) + " lbs")
elif kilorlbs == 'K' or 'k':
    result = weight * 2.2
    print("You weight " + str(result) + " kilograms")