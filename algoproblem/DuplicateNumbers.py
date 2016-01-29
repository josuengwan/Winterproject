insertion = '0123456789 01234 01234567890 6789012345 012322456789'.split()
for i in range(0,len(insertion)):
    comp = set(insertion[i])
    if len(insertion[i]) == len(comp) == 10:
        print("true")
    else:
        print("false")
