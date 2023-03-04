'''GCD_v1'''
def main(num, count=1):
    '''_'''
    num.sort()
    while num[0] != 0 and num[1] != 0:
        count += 1
        if count % 2 == 0:
            num[1] = num[1] % num[0]
        else:
            num[0] = num[0] % num[1]
    return max(num)

print(main([int(input()), int(input())]))
