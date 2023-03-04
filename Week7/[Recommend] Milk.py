"""[Recommend] Milk"""
def milk():
    """_"""
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    num_bottle = num_d//num_a
    num_cover = num_bottle
    while num_cover >= num_b and num_b > 0:
        temp1 = (num_cover//num_b)*num_c
        temp2 = num_cover%num_b
        num_bottle += temp1
        num_cover = temp1 + temp2
    print(num_bottle)
milk()
