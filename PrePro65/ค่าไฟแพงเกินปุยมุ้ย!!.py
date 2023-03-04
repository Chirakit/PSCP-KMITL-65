"""" ค่าไฟแพงเกินปุยมุ้ย!! """
def main():
    """ The goverment is uselesss ps.Why ejudge not allow for as string? it just a string"""
    num_0 = int(input())
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    num_4 = int(input())
    unit_0 = num_0 * 3 / 1000 * 30
    unit_1 = num_1 * 1 / 1000 * 30
    unit_2 = num_2 * 0.5 / 1000 * 30
    unit_3 = num_3 * 5 / 1000 * 30 * 4
    unit_4 = num_4 * 24 / 1000 * 30
    print("TV %d Watt 1 ea for 3 hours\n%.2f unit."%(num_0, unit_0))
    print("Microwave %d Watt 1 ea for 1 hours\n%.2f unit."%(num_1, unit_1,))
    print("Hair dryer %d Watt 1 ea for 0.5 hours\n%.2f unit."%(num_2, unit_2))
    print("light bulb %d Watt 4 ea for 5 hours\n%.2f unit."%(num_3, unit_3))
    print("Refrigerator %d Watt 1 ea for 24 hours\n%.2f unit."%(num_4, unit_4))
main()
