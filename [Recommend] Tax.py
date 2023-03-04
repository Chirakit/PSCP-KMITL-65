'''[Recommend] Tax'''
def station():
    '''_'''
    year = int(input())
    car = int(input())
    cost1, cost2, cost3 = 0, 0, 0
    if car >= 600:
        cost1 = 300
        if car >= 601:
            cost2 = 1800
            if car > 1800:
                cost3 = (car - 1800) * 4
    total = cost1 + cost2 + cost3
    if year == 6:
        print('%.2f'%(total-(total*(10/100))))
    elif year == 7:
        print('%.2f'%(total-(total*(20/100))))
    elif year == 8:
        print('%.2f'%(total-(total*(30/100))))
    elif year == 9:
        print('%.2f'%(total-(total*(40/100))))
    elif year >= 10:
        print('%.2f'%(total-(total*(50/100))))
    else:
        print('%.2f'%total)

station()
