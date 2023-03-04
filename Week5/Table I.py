"""Table I"""
def table():
    """_"""
    num = int(input())
    add_num = 0
    for _ in range(num):
        add_num += 1
        print("15 x %d = %d"%(add_num, add_num*15))
table()
