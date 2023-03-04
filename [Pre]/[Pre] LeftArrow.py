""" [Pre] LeftArrow """
def main():
    """ [Pre] LeftArrow """
    num_col = int(input())
    num_row = int(input())
    for iso in range(0, num_row):
        if iso <= (num_row // 2):
            print(" " * ((num_row // 2) - iso), end="")
            print("*" * num_col)
        else:
            print(" " * (iso - (num_row // 2)), end="")
            print("*" * num_col)
main()
