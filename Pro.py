'''Pro'''
def buffe():
    '''_'''
    come_x = int(input())
    pay_y = int(input())
    per_person_a = int(input())
    people_z = int(input())
    total = people_z * per_person_a
    if people_z >= come_x:
        dunno = 0
        while True:
            people_z -= pay_y
            dunno += 1
            if people_z <= pay_y:
                break
        discount = dunno * per_person_a
        print(total - discount)
    else:
        print(total)

buffe()
