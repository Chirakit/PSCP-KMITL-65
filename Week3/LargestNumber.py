"""LargestNumber"""
def largest():
    """_"""
    num1 = input()
    num2 = input()
    num3 = input()
    tot1 = int(num1 + num2 + num3)
    tot2 = int(num1 + num3 + num2)
    tot3 = int(num2 + num1 + num3)
    tot4 = int(num2 + num3 + num1)
    tot5 = int(num3 + num1 + num2)
    tot6 = int(num3 + num2 + num1)
    new1 = mac(tot1, tot2, tot3)
    new2 = mac(tot4, tot5, tot6)
    if new1 > new2:
        print(new1)
    else:
        print(new2)
def mac(sum_1, sum_2, sum_3):
    """_"""
    if sum_1 > sum_2 and sum_1 > sum_3:
        return sum_1
    elif sum_2 > sum_1 and sum_2 > sum_3:
        return sum_2
    elif sum_3 > sum_1 and sum_3 > sum_2:
        return sum_3
    else:
        return sum_1
largest()
