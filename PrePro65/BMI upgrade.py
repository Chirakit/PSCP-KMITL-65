""" BMI upgrade """
def main():
    """ in F F I out S"""
    weight = float(input())
    height = float(input())
    age = int(input())
    height_1 = height / 100
    bmi = weight / height_1 ** 2
    bmi = float("%.2f"%bmi)
    if age >= 18:
        if bmi < 16:
            print("Severe Thinness")
        elif bmi >= 16 and bmi <= 16.99:
            print("Moderate Thinness")
        elif bmi >= 17 and bmi <= 18.49:
            print("Mild Thinness")
        elif bmi >= 18.5 and bmi <= 24.99:
            print("Normal")
        elif bmi >= 25 and bmi <= 29.99:
            print("Overweight")
        elif bmi >= 30 and bmi <= 34.99:
            print("Obese Class I")
        elif bmi >= 35 and bmi <= 39.99:
            print("Obese Class II")
        elif bmi >= 40:
            print("Obese Class III")
    else:
        print("Please use BMI for Children and Teens.")
main()
