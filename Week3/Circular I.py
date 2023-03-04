'''Circular'''
def main():
    '''Circular'''
    me_x = float(input())
    me_y = float(input())
    r_machine = float(input())
    x_yu = float(input())
    y_yu = float(input())
    radius = ((x_yu - me_x)**2+(y_yu - me_y)**2)**0.5
    if radius <= r_machine:
        print("Yes")
    else:
        print("No")
main()
        