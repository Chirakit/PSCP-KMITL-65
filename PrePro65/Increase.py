""" Increase """
def main():
    """ I dunno """
    num = 0
    num_1 = 0
    total = 0
    while num >= 0:
        num = int(input())
        total += num
        if num < 0:
            num_1 -= num
            print(total + num_1)
main()
