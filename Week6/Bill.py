"""Bill"""
def bill():
    """_"""
    cost = int(input())
    charge = cost * 0.1#10%
    charge_lowest = 50
    charge_highest = 1000
    if charge < charge_lowest:
        tax = (cost + charge_lowest)*0.07
        print("%.2f"%(cost + charge_lowest + tax))
    elif charge > charge_highest:
        tax = (cost + charge_highest)*0.07
        print("%.2f"%(cost + charge_highest + tax))
    else:
        tax = (cost + charge)*0.07
        print("%.2f"%(cost + charge + tax))
bill()
