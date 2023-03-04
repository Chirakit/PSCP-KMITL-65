"""PointInCircle"""
import math
def input_thing():
    """_"""
    num_x = float(input())
    num_y = float(input())
    num_r = float(input())
    num_xn = float(input())
    num_yn = float(input())
    if math.sqrt((num_xn - num_x) ** 2 + (num_yn - num_y) ** 2) <= num_r:
        print("True")
    else:
        print("False")

input_thing()
