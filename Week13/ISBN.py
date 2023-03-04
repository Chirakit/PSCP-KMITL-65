'''ISBN'''
def main():
    '''_'''
    isbn = input()
    num1 = isbn[0:1]
    num2 = isbn[1:2]
    num3 = isbn[2:3]
    num4 = isbn[4:5]
    num5 = isbn[5:6]
    num6 = isbn[6:7]
    num7 = isbn[8:9]
    num8 = isbn[9:10]
    num9 = isbn[10:11]
    num10 = isbn[-1:]
    cal = (-1*((10*int(num1))+(9*int(num2))+(8*int(num3))+(7*int(num4))+(6*int(num5))+\
(5*int(num6))+(4*int(num7))+(3*int(num8))+(2*int(num9))))%11
    if num10 == 'X':
        if str(cal) == '10':
            print('Yes')
        else:
            print('No', 'X')
    elif num10 == str(cal):
        print('Yes')
    elif num10 != str(cal):
        if str(cal) == '10':
            print('No', 'X')
        else:
            print('No', str(cal))
main()
