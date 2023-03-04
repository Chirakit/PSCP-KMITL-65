'''Seeker'''
def main():
    '''seeker?'''
    txt = input()
    check = ''
    value = 0
    for i in txt:
        if i.isdigit() == True:
            check += i
        else:
            if check == '':
                value += 0
            else:
                value += int(check)
                check = ''
    if check.isdigit() == True:
        print(value + int(check))
    else:
        print(value)

main()
