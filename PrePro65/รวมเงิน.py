""" รวมเงิน """
def main():
    """ input str float """
    name_1 = input()
    name_2 = input()
    name_3 = ("%s %s"%(name_1, name_2))
    num_1 = float(input())
    num_2 = float(input())
    total = num_1 + num_2
    big_name = input()
    anything = input()
    print(name_3, total, big_name, sep=anything)
main()
