""" Toy Factory """
def main():
    """ magi toy """
    part_0 = input().replace("1", " ^----^")
    part_1 = input().replace("2", "( 0--0 )")
    part_2 = input().replace("3", "<------>")
    part_3 = input().replace("4", "(------)")
    part_4 = input().replace("5", " u----u")
    print(part_0.replace("5", " u----u"))
    print(part_1)
    print(part_2)
    print(part_3)
    print(part_4.replace("1", " ^----^"))
main()
