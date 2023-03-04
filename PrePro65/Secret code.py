""" Spy is in the base """
def main():
    """ Find him """
    secret = int(input())
    num_1 = secret // 100000# 5 ตำแหน่งแรก
    num_2 = secret % 100000# 5 ตำแหน่งหลัง
    num_3 = num_1 // 10# 4 ตำแหน่งแรก
    num_4 = num_3 % 10# ตำแหน่ง 2
    num_5 = num_3 // 100# 2 ตำแหน่งแรก
    num_6 = num_5 % 10# ตำแหน่งแรก
    num_7 = num_2 % 10# ตำแหน่ง 5
    num_8 = num_2 // 100# 3 ตำแหน่งหลัง
    num_9 = num_8 % 10# ตำแหน่ง 4
    num_10 = num_8 // 100# ตำแหน่ง 3
    print("%d%d%d%d%d"%(num_6, num_4, num_10, num_9, num_7))
main()
