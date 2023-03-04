"""Sequence VI"""
def sequence6():
    """_"""
    num = int(input())
    sum_add = 0
    for i in range(num):
        sum_add = 0
        for j in range(num):
            if i < j:
                print(" ", end=" ")
            else:
                sum_add += 1
                print(sum_add, end=" ")
        print()
sequence6()
