"""Sequence VIII"""
def sequence8():
    """_"""
    num = int(input())
    for i in range(0, num):
        for j in range(0, num):
            if i+j >= num-1:
                print("%02d"%((i+j)-(num-2)), end=" ")
            else:
                print(" ", end="  ")
        print()
sequence8()
