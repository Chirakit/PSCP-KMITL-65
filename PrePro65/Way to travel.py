""" Way to travel """
def main():
    """ if - = error """
    weather = input()
    imp_1 = input()
    sum_1 = float(input())
    if weather == "rainy" and imp_1 == "important":
        if sum_1 >= 300:
            print("Private jet")
        elif sum_1 < 300 and sum_1 >= 20:
            print("Car")
        elif sum_1 < 20 and sum_1 >= 1:
            print("Motorcycle")
        elif sum_1 < 1 and sum_1 >= 0:
            print("Walk")
        elif sum_1 < 0:
            print("Error")
        else:
            print("Not go")
    elif weather == "sunny" and imp_1 == "important" or "not important":
        if sum_1 >= 300:
            print("Private jet")
        elif sum_1 < 300 and sum_1 >= 20:
            print("Car")
        elif sum_1 < 20 and sum_1 >= 1:
            print("Motorcycle")
        elif sum_1 < 1 and sum_1 >= 0:
            print("Walk")
main()
