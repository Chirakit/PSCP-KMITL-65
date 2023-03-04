"""Calculator"""
def calculator():
    """_"""
    press = int(input())
    txt = ""
    if press == 1:
        print(press)
    else:
        for i in range(press):
            i += 1
            txt += str(i)+"+"
        print(len(str(txt)))

calculator()
