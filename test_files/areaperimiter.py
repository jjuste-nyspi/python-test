def area_or_perimeter(l , w):
    if l == w:
        result = l * w
        print("I am a square")
        print(result)
    else:
        perimeter = 2 * (l + w)
        print("I am a rectangle")
        print(perimeter)

area_or_perimeter(6,10)