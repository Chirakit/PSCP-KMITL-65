"""HideAndSeek"""
def count():
    """_"""
    num_start = int(input())
    num_end = int(input())
    num_step = int(input())
    for i in range(num_start, num_end, num_step):
        print(i)
count()
