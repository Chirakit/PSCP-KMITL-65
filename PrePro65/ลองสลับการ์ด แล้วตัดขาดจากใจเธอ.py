""" ลองสลับการ์ด แล้วตัดขาดจากใจเธอ """
def main():
    """ puzzle? """
    num_1 = int(input())
    if num_1 == 12 or num_1 == 21:
        print("A")
    elif num_1 == 13 or num_1 == 31:
        print("B")
    elif num_1 == 23 or num_1 == 32:
        print("C")
main()
