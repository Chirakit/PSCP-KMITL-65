'''FibonacciRecursionV1'''
def fibonacci(num):
    '''_'''
    if num in {0, 1}:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

def main():
    '''_'''
    print((fibonacci(int(input()))))

main()
