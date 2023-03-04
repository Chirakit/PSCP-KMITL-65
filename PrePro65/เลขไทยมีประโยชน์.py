""" เลขไทยมีประโยชน์ """
def main():
    """ That not fair """
    thai = input()#Y/N
    age = int(input())
    discount = input()#Y/N
    cost_0 = 20
    cost_1 = 40
    cost_for0 = cost_0 * 5
    cost_for1 = cost_1 * 5
    if thai == "Y":
        if discount == "Y":
            dis_per = int(input())
            if 20 >= age > 10:
                print(cost_0 // (dis_per / 100))
            elif 60 >= age > 20:
                print(cost_1 - (cost_1 // (dis_per / 100)))
            elif 60 < age <= 10:
                print(0)
        elif discount == "N":
            if 20 >= age > 10:
                print(cost_0)
            elif 60 >= age > 20:
                print(cost_1)
            elif 60 < age <= 10:
                print(0)
main()
