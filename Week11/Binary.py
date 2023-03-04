'''Binary'''
def nary():
    '''_'''
    num = int(input())
    total = ''
    while num >= 2:
        total += str(num % 2)
        num //= 2
    total += str(num)
    total = total[::-1]
    print(total)
 
nary()
