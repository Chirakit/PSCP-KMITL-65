'''One For All'''
def once():
    '''_'''
    people = int(input())
    rank = 0
    more = ''
    if people > 0:
        for _ in range(people):
            name = input()
            rank += 1
            if rank == people:
                continue
            if rank % 2 == 0:
                member = name+('-'*rank)
                more += member
            else:
                member = name+('*'*rank)
                more += member
        print(more+name, end='_'+str(rank))
    else:
        pass

once()
