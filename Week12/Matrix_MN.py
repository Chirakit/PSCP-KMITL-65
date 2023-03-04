'''Matrix_MN'''
def main():
    '''_'''
    row = int(input())
    col = int(input())
    area = row*col
    marx = []
    for i in range(area):
        num = input()
        marx.append(num)
    frq = 0
    for i in marx:
        print(i, end=" ")
        frq += 1
        if frq == col:
            print()
            frq = 0
main()
