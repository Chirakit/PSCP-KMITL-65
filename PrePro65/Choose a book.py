""" Choose a book """
import math
def main():
    """ Forgot """
    sum_n = int(input())
    sum_n2 = (math.factorial(sum_n))
    sum_r = int(input())
    sum_r2 = (math.factorial(sum_r))
    total = int(sum_n2 / (sum_r2 * (math.factorial(sum_n - sum_r))))
    print(total)
main()
