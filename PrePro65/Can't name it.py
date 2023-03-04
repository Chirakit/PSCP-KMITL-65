""" Binaryปิด/เปิด """
def main():
    """ 00110001 00110000 01101100 01100101 01100110 01110100 """
    num_1 = bin(int(input()))
    num_1 = num_1[2:]
    print(num_1.replace("1", "open, ").replace("0", "close, ").strip(", "))
main()
