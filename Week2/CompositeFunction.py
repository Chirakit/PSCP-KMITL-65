"""CompositeFunction"""
def main():
    """_"""
    num = int(input())
    total(num)
def total(num):
    """_"""
    total1 = 2*num
    total2 = num/2+1
    factiom1(total2)
    factiom2(total1)
def factiom2(total1):
    """_"""
    total2 = total1/2+1
    print("%.2f"%total2)
def factiom1(total2):
    """_"""
    total1 = 2*total2
    print("%.2f"%total1)
main()
