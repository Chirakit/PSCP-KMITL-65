""" We gonna be rich """
def main():
    """ It's Payday time """
    money = float(input())
    cost = float(input())
    total_1 = money - cost
    coin_1 = total_1 // 10
    total_2 = total_1 - coin_1 * 10
    coin_2 = total_2 // 5
    total_3 = total_2 - coin_2 * 5
    coin_3 = total_3 // 2
    total_4 = total_3 - coin_3 * 2
    coin_4 = total_4 // 1
    total_5 = total_4 - coin_4 * 1
    coin_5 = total_5 // 0.5
    total_6 = total_5 - coin_5 * 0.5
    total_6 = total_6
    most_coin = total_1 // 0.25
    less_coin = coin_1 + coin_2 + coin_3 + coin_4 + coin_5
    print("%d\n%d\n%.1f"%(most_coin, less_coin, total_1))
main()
