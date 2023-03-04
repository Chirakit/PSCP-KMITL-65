""" Find v """
def main():
    """ s(float) t(int) สูตร v = s / t """
    long_1 = float(input()) #s 1 ไมล์ทะเล = 1852 m
    time_1 = int(input()) #t 1 มิลลิวิ = 0.001 วิ
    long_2 = long_1 * 1852
    time_2 = time_1 * 0.001
    print("อัตราเร็วเท่ากับ : %.3f เมตรต่อวินาที"%(long_2 / time_2))
main()
