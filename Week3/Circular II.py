"""Circular II"""
def main():
    """_"""
    my_x = float(input())
    my_y = float(input())
    my_machine = float(input())
    x_you = float(input())
    y_you = float(input())
    friend_machine = float(input())
    radius = ((x_you - my_x)**2+(y_you - my_y)**2)**0.5
    if radius < my_machine+friend_machine:
        print("Yes")
    else:
        print("No")
main()
