""" BMI TEST """
def main():
    """ input(int) output(float) """
    name = input()
    weight = int(input()) #kg
    height_1 = int(input()) #cm
    height_2 = float(height_1 / 100)
    print("Name: %s\nWeight: %d kg.\nHeight: %.2f m.\nBMI: %.2f\n"%(name, weight, \
        height_2, weight / height_2 ** 2))
main()
