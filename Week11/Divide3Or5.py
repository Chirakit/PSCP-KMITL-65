'''Divide3Or5'''
def main():
    '''_'''
    num = float(input())
    more = 0
    for i in range(1, int(num)+1):
        if i % 3 == 0 or i % 5 == 0:
            more += i
    print(more)
main()
