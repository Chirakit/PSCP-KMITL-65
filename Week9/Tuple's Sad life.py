"""Tuple's Sad life"""
def life():
    """_"""
    num = tuple(input().split(" "))
    goal_num = input()
    find_index = num.index(goal_num)
    count_num = num.count(goal_num)
    for _ in range(count_num):
        for _ in range(count_num):
            print(find_index, end=" ")
        print()
life()
