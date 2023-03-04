"""Sequence N"""
def sequence():
    """_"""
    num = int(input())
    for i in range(num):
        print("*")
        for j in range(i):
            print("*", end="")
sequence()
