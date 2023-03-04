"""BTSMRT"""
def train():
    """_"""
    day = input()
    age = float(input())
    high = float(input())
    if day == "Children Day":
        if age < 14 and high <= 140:
            print("FREE")
        else:
            print("PAY")
    elif day == "Senior Day":
        if age >= 60:
            print("FREE")
        elif age < 14 and high < 90:
            print("FREE")
        else:
            print("PAY")
    else:
        if age < 14 and high < 90:
            print("FREE")
        else:
            print("PAY")
train()
