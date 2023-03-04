"""Sequence IV"""
def sequence4():
    """input_num"""
    num = int(input())
    sum_for_add = 0
    for _ in range(num):
        for _ in range(num):
            sum_for_add += 1
            print(sum_for_add, end=' ')
        print()
sequence4()
