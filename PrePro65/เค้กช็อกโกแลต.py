""" เค้กช็อกโกแลต """
def main():
    """ I'm hungry """
    money = int(input())
    cost = int(input())
    if money >= cost:
        total = (money // cost) * cost
        print("Chocolate Cake: %d\nMoney left: %d"%(money // cost, money - total))
    else:
        print("Not enough money;(\nMoney left: %d"%(money))
main()
