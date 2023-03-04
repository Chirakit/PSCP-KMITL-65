"""Virus I"""
def t_virus():
    """_"""
    virus = input()
    num = len(virus)
    for i in virus:
        if i == "O":
            num -= 1
    print(num)
t_virus()
#ทำให้เสร็จนะครับ
