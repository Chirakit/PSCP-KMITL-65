"""Sequence III"""
def sequence():
    """_"""
    num = int(input())
    begin = 1
    for _ in range(begin, num+1):
        for _ in range(begin, num+1):
            print(_ + 1, end=" ")
        num += 1
        begin += 1
        _ += 1
        print()
sequence()
