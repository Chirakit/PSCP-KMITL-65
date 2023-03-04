"""Jumping"""
def jumping():
    """_"""
    num = 0
    for _ in range(4):
        num += 1
        print_output(num)

def print_output(num):
    """_"""
    for _ in range(3):
        print("Output%d"%num)
jumping()
