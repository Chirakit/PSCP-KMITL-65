"""Future Message"""
def future():
    """_"""
    txt = input()
    if txt.isnumeric() == True:
        print("Number")
    elif txt.isupper() == True:
        print("Uppercase")
    elif txt.islower() == True:
        print("Lowercase")
    elif txt.istitle() == True:
        print("Title")
    elif txt.isspace() == True:
        print("Space")
    else:
        print("Other")
future()
