"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def info():
    """_"""
    way = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if way == "Ascend":
        if num1 < num2 and num1 < num3:
            if num2 < num3 and num2 > num1:
                print("%.2f, %.2f, %.2f"%(num1, num2, num3))
            else:
                print("%.2f, %.2f, %.2f"%(num1, num3, num2))
        elif num2 < num1 and num2 < num3:
            if num1 < num3 and num1 > num2:
                print("%.2f, %.2f, %.2f"%(num2, num1, num3))
            else:
                print("%.2f, %.2f, %.2f"%(num2, num3, num1))
        elif num3 < num2 and num3 < num1:
            if num2 < num1 and num2 > num3:
                print("%.2f, %.2f, %.2f"%(num3, num2, num1))
            else:
                print("%.2f, %.2f, %.2f"%(num3, num1, num2))
    descend(way, num1, num2, num3)
    ascend(way, num1, num2, num3)
    desssend(way, num1, num2, num3)
def descend(way, num1, num2, num3):
    """_"""
    if way == "Descend":
        if num1 > num2 and num1 > num3:
            if num2 > num3 and num2 < num1:
                print("%.2f, %.2f, %.2f"%(num1, num2, num3))
            else:
                print("%.2f, %.2f, %.2f"%(num1, num3, num2))
        elif num2 > num1 and num2 > num3:
            if num1 > num3 and num1 < num2:
                print("%.2f, %.2f, %.2f"%(num2, num1, num3))
            else:
                print("%.2f, %.2f, %.2f"%(num2, num3, num1))
        elif num3 > num2 and num3 > num1:
            if num2 > num1 and num2 < num3:
                print("%.2f, %.2f, %.2f"%(num3, num2, num1))
            else:
                print("%.2f, %.2f, %.2f"%(num3, num1, num2))
def ascend(way, num1, num2, num3):
    """_"""
    if way == "Ascend":
        if num1 == num2 and num1 == num3:
            print("%.2f, %.2f, %.2f"%(num1, num2, num3))
        elif num1 == num2 and num1 < num3:
            print("%.2f, %.2f, %.2f"%(num1, num2, num3))
        elif num2 == num3 and num2 < num1:
            print("%.2f, %.2f, %.2f"%(num2, num3, num1))
        elif num1 == num3 and num1 < num2:
            print("%.2f, %.2f, %.2f"%(num1, num3, num2))
def desssend(way, num1, num2, num3):
    """_"""
    if way == "Descend":
        if num1 == num2 and num1 == num3:
            print("%.2f, %.2f, %.2f"%(num1, num2, num3))
        elif num1 == num2 and num3 < num1:
            print("%.2f, %.2f, %.2f"%(num1, num2, num3))
        elif num2 == num3 and num1 < num2:
            print("%.2f, %.2f, %.2f"%(num2, num3, num1))
        elif num1 == num3 and num2 < num1:
            print("%.2f, %.2f, %.2f"%(num1, num3, num2))
        elif num1 == num2 and num3 > num1:
            print("%.2f, %.2f, %.2f"%(num3, num2, num1))
        elif num2 == num3 and num1 > num2:
            print("%.2f, %.2f, %.2f"%(num1, num3, num2))
        elif num1 == num3 and num2 > num1:
            print("%.2f, %.2f, %.2f"%(num2, num3, num1))
info()
