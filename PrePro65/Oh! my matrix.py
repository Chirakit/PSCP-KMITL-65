""" What is matrix? """
def main():
    """" kinda forget it """
    a_1 = int(input())#a1
    a_2 = int(input())#a2
    a_3 = int(input())#a3
    a_4 = int(input())#a4
    c_1 = int(input())#c1
    c_2 = int(input())#c2
    c_3 = int(input())#c3
    c_4 = int(input())#c4
    b_1 = c_1 - a_1
    b_2 = c_2 - a_2
    b_3 = c_3 - a_3
    b_4 = c_4 - a_4
    total_1 = (a_1 * a_4) - (a_3 * a_2)
    total_2 = (c_1 * c_4) - (c_3 * c_2)
    total_3 = (b_1 * b_4) - (b_3 * b_2)
    print("b1: %d\nb2: %d\nb3: %d\nb4: %d\nD: %.2f"%(b_1, b_2, b_3, b_4, total_1 + total_2 + \
        total_3))
main()
