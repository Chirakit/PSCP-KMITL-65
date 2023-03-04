"""BootSequence"""
def boot():
    """_"""
    num = int(input())
    for i in range(num):
        print(i+1, end="")
        if i+1 < num:
            print("_", end="")
boot()
