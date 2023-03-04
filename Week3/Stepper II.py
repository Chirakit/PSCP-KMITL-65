"""Stepper II"""
def step2():
    """_"""
    num_start = int(input())
    num_end = int(input())
    total = ((num_start - num_end)*-1)+1
    if total < 0:
        for _ in range(total*-1+2):
            print(num_start)
            num_start -= 1
    else:
        for _ in range(total):
            print(num_start)
            num_start += 1
step2()
