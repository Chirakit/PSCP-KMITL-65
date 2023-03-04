""" อักษรที่หายไป """
def main():
    """ ayo """
    text_1 = input()
    traget = text_1.find('"')
    traget_0 = text_1.rfind('"')
    if text_1.find('"') == -1:
        print("No error")
    else:
        num_0 = chr(int(text_1[traget + 1:traget_0]))
        print(text_1[:traget] + num_0 + text_1[traget_0 + 1:])
main()
