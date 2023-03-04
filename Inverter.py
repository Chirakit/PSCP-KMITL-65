def loop_bi():
    '''_'''
    num = int(input())
    ans = ''
    for i in num:
        if i == '1':
            ans += '0'
        else:
            ans += '1'
    print(num)
loop_bi()
