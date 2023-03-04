"""Elo"""
def dota2():
    """LOL_is_better"""
    num_ra = int(input())
    num_rb = int(input())
    team = input()
    if team == "A":
        possibility = 1/(1+10**((num_rb-num_ra)/400))
        print("%.2f"%possibility)
    elif team == "B":
        possibility = 1/(1+10**((num_ra-num_rb)/400))
        print("%.2f"%possibility)
dota2()
