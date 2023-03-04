""" How many """
def main():
    """ HOW """
    text_1 = input()
    traget = input()
    text_2 = text_1.lower()
    traget_1 = traget.lower()
    if len(traget) == 1:
        if text_2.count(traget_1) != 0:
            print("Character : %d"%(text_2.count(traget_1)))
        else:
            print("No word and character.")
    elif len(traget) > 1:
        if text_2.count(traget_1) != 0:
            print("Word : %d"%(text_2.count(traget_1)))
        else:
            print("No word and character.")
main()
