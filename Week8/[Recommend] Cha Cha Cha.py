'''[Recommend] Cha Cha Cha'''
import math
def cha():
    '_'
    day = int(input())
    money_per_hour = 8720
    total = 0
    for _ in range(day):
        hour = math.ceil(float(input()))
        slary = money_per_hour * hour
        total += slary
    print(total)

cha()
