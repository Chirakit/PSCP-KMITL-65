'''Pringles'''
def nice():
    '''_'''
    size_1 = input()
    chip = input()
    size_2 = input()
    hand = int(input())
    result = ""
    count_1 = 0
    for i in chip[:hand]:
        if i == ")":
            result += " "
            count_1 += 1
        else:
            result += " "
    result = result+chip[hand:]
    print(count_1)
    if result.count(")") > 0:
        print("There are still some left.")
    else:
        print("None.")
    print(size_1, result, size_2, sep="\n")
nice()
