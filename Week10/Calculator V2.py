'''Calculator V2'''
def math(cal):
    '''_'''
    if cal <= 1:
        return 1
    word_length, result = len(str(cal)), 0
    for i in range(word_length):
        start_num, end_num = int('1' + '0'*(i-1)), int('9' + '9'*(i-1))
        result += i * (end_num - start_num + 1)
        last_run = 10**i
    return result + cal + (word_length * (cal-last_run+1))

print(math(int(input())))
