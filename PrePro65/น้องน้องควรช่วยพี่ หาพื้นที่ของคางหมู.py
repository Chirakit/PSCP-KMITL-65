""" หาพื้นที่ของคางหมู """
def main():
    """ all float """
    hight = float(input())
    base_1 = float(input())
    base_2 = float(input())
    base = base_1 + base_2
    print("Trapezoidal area = %.2f"%(0.5 * hight * base))
main()
