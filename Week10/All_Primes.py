'''All_Primes'''
def prime_1(thisnum):
    '''_'''
    prime = True
    if thisnum >= 2:
        for i in range(2, thisnum):
            if thisnum % i == 0:
                prime = False
                break
    else:
        prime = False
    return prime

def main(num1, count=0):
    '''_'''
    for i in range(2, num1+1):
        if prime_1(i):
            count += 1
    print(count)

main(int(input()))
