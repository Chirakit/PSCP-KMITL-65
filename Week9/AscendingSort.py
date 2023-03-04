'''AscendingSort'''
def main():
    '''_'''
    value = []
    for _ in range(5):
        num = int(input())
        value.append(num)
    value.sort()
    print(*value, sep="\n")
main()
