"""Timing II"""
def main():
    """Timing II"""
    sec = int(input())
    mini = sec//60
    sec = sec%60
    hour = mini//60
    mini = mini%60
    day = hour//24
    hour = hour%24
    if day > 9999:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d"%(day, hour, mini, sec))
main()
