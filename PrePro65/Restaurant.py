""" Restaurant """
def main():
    """ >60 = FREE 1 """
    age = int(input())
    plate = int(input())
    cost = 100
    if age >= 60 and plate == 1:
        print("Free")
    elif age >= 60 and plate > 1:
        print("Pay %d baht"%((plate * cost) * 50 / 100))
    else:
        print("Pay %d baht"%(plate * cost))
main()
