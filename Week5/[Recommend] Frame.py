"""Frame"""
def frame():
    """_"""
    txt = input()
    how = len(txt)
    new = txt.center(how+2, "*")
    more_new = len(new)
    print("*"*more_new)
    print(new)
    print("*"*more_new)
frame()
