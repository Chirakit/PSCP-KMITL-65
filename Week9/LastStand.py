'''LastStand'''
def last():
    '''_'''
    value = input()
    value = value.replace("[", "")
    value = value.replace("]", "")
    value = value.split(",")
    for text in value:
        print(text[-1])
last()
