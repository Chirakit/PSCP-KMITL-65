""" Fast server """
def main():
    """ all int """
    time_1 = int(input())
    etc_1 = input()
    time_2 = int(input())
    etc_2 = input()
    sec_0 = time_1 / 1000#Millisecond
    sec_1 = time_1 / 1000000#Microsecond
    sec_2 = time_1 / 1000000000#Nanosecond
    sec_3 = time_1 / 1000000000000#Picosecond
    sec_4 = time_2 / 1000#Millisecond
    sec_5 = time_2 / 1000000#Microsecond
    sec_6 = time_2 / 1000000000#Nanosecond
    sec_7 = time_2 / 1000000000000#Picosecond
    if etc_1 == "Millisecond" and etc_2 == "Nanosecond":
        if sec_0 < sec_6:
            timetotal = sec_6 // sec_0
            print("Server A, %.6f second\nFaster than server B , %d times"%(sec_0, timetotal))
        elif sec_6 < sec_0:
            timetotal = sec_0 // sec_6
            print("Server B, %.6f second\nFaster than server A , %d times"%(sec_6, timetotal))
        else:
            print("equal")
    elif etc_1 == "Microsecond" and etc_2 == "Millisecond":
        if sec_1 < sec_4:
            timetotal = sec_4 // sec_1
            print("Server A, %.6f second\nFaster than server B , %d times"%(sec_1, timetotal))
        elif sec_4 < sec_1:
            timetotal = sec_1 // sec_4
            print("Server B, %.6f second\nFaster than server A , %d times"%(sec_4, timetotal))
        else:
            print("equal")
    elif etc_1 == "Picosecond" and etc_2 == "Microsecond":
        if sec_3 < sec_5:
            timetotal = sec_5 // sec_3
            print("Server A, %.6f second\nFaster than server B , %d times"%(sec_3, timetotal))
        elif sec_5 < sec_3:
            timetotal = sec_3 // sec_5
            print("Server B, %.6f second\nFaster than server A , %d times"%(sec_5, timetotal))
        else:
            print("equal")
main()
