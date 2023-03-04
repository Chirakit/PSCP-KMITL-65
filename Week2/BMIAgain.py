"""BMIAgain"""
def bmi():
    """_"""
    weight = float(input())
    height = float(input())
    cal_bmi = weight/((height/100)**2)
    if cal_bmi >= 30:
        print("Obese")
    elif 25 <= cal_bmi < 30:
        print("Overweight")
    elif 18.5 <= cal_bmi < 25:
        print("Normal")
    else:
        print("Underweight")
bmi()
