"""Sequence V"""
def sequence5():
    '''_'''
    num = int(input())+1
    if (num-1) % 7 == 0:
        for _ in range(num//7):
            for _ in range(num, num-7, -1):
                print(_-1, end=' ')
                num -= 1
            print()
    else:
        for _ in range(num//7+1):
            for _ in range(num, num-7, -1):
                print(_-1, end=' ')
                num -= 1
                if _ == 2:
                    break
            print()
sequence5()
