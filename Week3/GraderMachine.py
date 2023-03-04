"""GraderMachine"""
def meth():
    """_"""
    num_start = int(input())
    num_end = int(input())
    total = 0
    print("pass :", end=" ")
    if num_end >= num_start:
        for i in range(num_start, num_end+1):
            if i % 2 == 0:
                print(i, end=" ")
                total += i
    else:
        for i in range(num_start, num_end-1, -1):
            if i % 2 == 0:
                print(i, end=" ")
                total += i
    print()
    print("Sum :", total)
meth()
