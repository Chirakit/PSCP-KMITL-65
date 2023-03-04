"""Parity"""
def parity():
    """_"""
    bits = input()
    evenorodd = input()
    num = 0
    for i in bits:
        if i == "1":
            num += 1
    if evenorodd == "Even":
        if num%2 == 0:
            print(bits+"0")
        else:
            print(bits+"1")
    else:
        if num%2 == 0:
            print(bits+"1")
        else:
            print(bits+"0")
parity()
