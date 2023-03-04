"""DataSpike"""
def input_sum():
    """_"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    num6 = int(input())
    num7 = int(input())
    num8 = int(input())
    var1 = find_mac(num1, num2)
    var2 = find_mac(var1, num3)
    var3 = find_mac(var2, num4)
    var4 = find_mac(var3, num5)
    var5 = find_mac(var4, num6)
    var6 = find_mac(var5, num7)
    var7 = find_mac(var6, num8)
    print(var7)
def find_mac(sum_1, sum_2):
    """_"""
    if sum_1 > sum_2:
        return sum_1
    else:
        return sum_2
input_sum()
