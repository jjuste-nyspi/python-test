def duplicate_characters(string):
    lowerstring = string.lower()
    chars = {}

    # iterate through string
    for char in lowerstring:
        if char not in chars:
            chars[char] = 1
        else:
            #if the character is already in the dictionary, increment the count
            chars[char] += 1

    # list to store chars
    duplicates = []

    # iterate through dictionary to find characters with count greater than 1
    for char, count in chars.items():
        if count > 1:
            duplicates.append(char)
    return len(duplicates)

print(duplicate_characters('abcdeaB'))
