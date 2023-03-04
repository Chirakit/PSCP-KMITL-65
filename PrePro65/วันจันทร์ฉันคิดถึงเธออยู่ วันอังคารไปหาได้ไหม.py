"""" miss u everyday """
def main():
    """ int only """
    second = int(input())
    second_1 = second % (24 * 3600)
    day = second // 86400
    hour = second_1 // 3600
    hour_1 = second % 3600
    minute = hour_1 // 60
    sec = hour_1 % 60
    print("%02d:%02d:%02d:%02d"%(day, hour, minute, sec))
main()
