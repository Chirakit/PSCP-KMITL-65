""" yes or no """
def main():
    """ I want to play payday2 now """
    text_1 = input()
    xox = str(min(text_1))
    aoa = ord(xox)
    if aoa >= 32 and aoa <= 47:
        print("No, it's not.")
    else:
        print("Yes, it is.")
main()
