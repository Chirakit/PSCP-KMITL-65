"""BrickBridge"""
def brick():
    """_"""
    small_brick = int(input())
    big_brick = int(input())
    goal = int(input())
    only_big = goal // 5
    if big_brick > only_big:
        big_brick = only_big
    goal -= big_brick * 5
    if goal > small_brick:
        print(-1)
    else:
        print(goal)
brick()
