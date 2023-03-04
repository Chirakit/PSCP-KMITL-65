'''WordSequence I'''
def main(txt):
    '''_'''
    for i in range(1, len(txt)+1):
        for j in txt[:i]:
            print(j, end='')
        print()

main(str(input()))
