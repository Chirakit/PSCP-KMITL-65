"""Harshad"""
def harshad():
    """_"""
    num = int(input())
    total = 0
    for _ in range(10):
        if len(str(num)) == 2:
            for i in str(num):
                total += int(i)
                if num % total == 0:
                    print("Yes")
                else:
                    print("No")
        print("Yes")
harshad()
