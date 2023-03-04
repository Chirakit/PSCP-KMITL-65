'''CoPrimeV1'''
def main():
    '''_'''
    num_1 = int(input())
    num_2 = int(input())
    ans = main_1([num_1, num_2])
    if ans == 1:
        print('YES')
    else:
        print('NO')
    print(ans)

def main_1(num, count=1):
    '''_'''
    num.sort()
    while num[0] != 0 and num[1] != 0:
        count += 1
        if count % 2 == 0:
            num[1] = num[1] % num[0]
        else:
            num[0] = num[0] % num[1]
    return max(num)

main()
