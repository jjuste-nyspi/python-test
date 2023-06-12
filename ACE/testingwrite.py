def abbrev_name(name):
    a = name.split()
    b = [item[0] for item in a]
    c = [i.upper() for i in b]
    d = ".".join(c)
    print(d)

abbrev_name("Sam Harris")
abbrev_name("patrick feenan")
abbrev_name("Evan C")
abbrev_name("P Favuzzi")
abbrev_name("David Mendieta")