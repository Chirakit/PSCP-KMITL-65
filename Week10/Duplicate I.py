'''Duplicate'''
def duplicate():
    '''_'''
    num_a = int(input())
    num_b = int(input())
    set_a = set()
    set_b = set()
    for _ in range(num_a):
        sum_0 = int(input())
        set_a.add(sum_0)
    for _ in range(num_b):
        sum_1 = int(input())
        set_b.add(sum_1)
    if set_a.isdisjoint(set_b) == True:
        print("Nope")
    else:
        ans = set_a.intersection(set_b)
        ans = sorted(ans)
        for i in ans[::-1]:
            print(i)

duplicate()
