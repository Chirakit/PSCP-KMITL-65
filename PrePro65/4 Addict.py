""" main Jhin """
def main():
    """ ติด 4 """
    sum_1 = float(input())
    word = input()
    dia = ((((sum_1 + 4) ** (1/4)) + (sum_1 / 4)) / (4 * sum_1 - 4)) * 44
    per = int(sum_1 // 44)
    print("%s\n%.4f"%(word * per, dia))
main()
