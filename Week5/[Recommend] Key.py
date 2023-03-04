"""Key"""
def key():
    """_"""
    num_id = input()
    total = 0
    for i in num_id:
        i = int(i)
        total += i
    total_num = total
    last_3 = (int(num_id) % 1000) * 10
    ans = last_3 + total_num
    member = len(str(ans))
    if ans < 1000:
        print(ans + 1000)
    elif member > 4:
        print(str(ans)[1:])
    else:
        print(ans)
key()
