'''WordSequence II'''
def sequence(txt_1, txt_2):
    '''_'''
    temp = txt_1
    for i in range(1, len(txt_2)+2):
        print(temp)
        temp = txt_2[:i] + txt_1[i:]
        lastrun = txt_1[i:]
    if temp == txt_2:
        return 0
    txt_1 = lastrun
    if len(txt_1) > len(txt_2):
        for i in range(len(txt_1)+1):
            temp = txt_2 + txt_1[i:]
            print(temp)

sequence(input(), input())
