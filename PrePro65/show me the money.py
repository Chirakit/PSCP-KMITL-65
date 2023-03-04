""" show me the money """
def main():
    """ hmmm """
    money = float(input())
    cost = float(input())
    if money == cost:
        print("จ่ายมาพอดี")
    elif money > cost:
        total = money - cost
        coin_1 = total // 100
        coin_2 = total % 100 // 50
        coin_3 = total % 100 % 50 // 20
        coin_4 = total % 100 % 50 % 20 // 12
        coin_5 = total % 100 % 50 % 20 % 12 // 10
        coin_6 = total % 100 % 50 % 20 % 12 % 10 // 5
        coin_7 = total % 100 % 50 % 20 % 12 % 10 % 5 // 2
        coin_8 = total % 100 % 50 % 20 % 12 % 10 % 5 % 2 // 1
        coin_9 = total % 100 % 50 % 20 % 12 % 10 % 5 % 2 % 1 // 0.5
        coin_10 = total % 100 % 50 % 20 % 12 % 10 % 5 % 2 % 1 % 0.5 // 0.25
        print("เเบงค์ 100 บาท : %d\nเเบงค์ 50 บาท : %d\nเเบงค์ 20 บาท : %d\nเหรียญ 12 บาท : %d\n\
เหรียญ 10 บาท : %d\nเหรียญ 5 บาท : %d\nเหรียญ 2 บาท : %d\nเหรียญ 1 บาท : %d\nเหรียญ 50 สตางค์ : %d\n\
เหรียญ 25 สตางค์ : %d"%(coin_1, coin_2, coin_3, coin_4, \
coin_5, coin_6, coin_7, coin_8, coin_9, coin_10))
    else:
        print("จำนวนเงินไม่พอ")
main()
