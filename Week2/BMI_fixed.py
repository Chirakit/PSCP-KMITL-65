"""BMI"""
def info():
    """input info"""
    name = input()
    weigh = float(input())
    heigh = float(input())
    return"%s's  BMI = %.2f"%(name, weigh/((heigh/100)**2))

print(info(), info(), info(), info(), info(), sep="\n")
