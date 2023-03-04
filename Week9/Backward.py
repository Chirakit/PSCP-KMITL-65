"""Backward"""
def backward():
    """TENET"""
    new_txt = []
    while True:
        txt = input()
        if txt == 'NULL':
            break
        new_txt.append(txt)
    new_txt.reverse()
    print(''.join(i for i in new_txt))
backward()
