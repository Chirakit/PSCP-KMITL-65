'''OneTwo'''
def cal(num):
    '''_'''
    if num in {1}:
        return '1'
    elif num in {2}:
        return '2'
    return cal(num - 1) + cal(num - 2)

def main():
    '''_'''
    print(cal(int(input())))

main()
