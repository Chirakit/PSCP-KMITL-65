"""Grade III"""
def main_grade(num):
    """_"""
    if num > 100 or num < 0:
        num = 0
    elif num >= 95:
        num = 4
    elif num >= 90:
        num = 3.5
    elif num >= 85:
        num = 3
    elif num >= 80:
        num = 2.5
    elif num >= 75:
        num = 2
    elif num >= 70:
        num = 1.5
    elif num >= 65:
        num = 1
    elif num >= 60:
        num = 0.5
    elif num >= 0:
        num = 0
    return num

def grade():
    """_"""
    subject = int(input())
    ur_grade = 0
    oh_grade = 0
    for _ in range(subject):
        score = int(input())
        ur_grade = main_grade(score)
        oh_grade += ur_grade
    print("%.2f"%(oh_grade / subject))
grade()
