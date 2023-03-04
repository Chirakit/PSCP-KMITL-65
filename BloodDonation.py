'''BloodDonation'''
def desk():
    '''What we need?'''
    age = int(input())
    weight = int(input())
    donate = int(input())
    if age == 17 or age >= 60 and age <= 70:
        agreement = input()
        if agreement == 'True':
            if weight >= 45:
                if donate > 0:
                    print('Yes')
                elif age >= 55:
                    print('No')
                else:
                    print('Yes')
            else:
                print('No')
        else:
            print('No')
    elif age > 17 and age <= 59:
        if weight >= 45:
            if donate > 0:
                print('Yes')
            elif age >= 55:
                print('No')
            else:
                print('Yes')
        else:
            print('No')
    else:
        print('No')
desk()
