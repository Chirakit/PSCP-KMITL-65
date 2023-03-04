""" ProfileAgain """
def main():
    """ Sorry for forgoting docstring """
    sex = input()
    num_1 = input()
    name_1 = input()
    surename = input()
    age = int(input())
    job = input()
    sex_0 = sex.lower()
    sex_1 = sex_0.replace("female", "Mrs.")
    print("=" * 6)
    print("ID :", num_1[:6])
    print("Name :", sex_1.replace("male", "Mr."), name_1.capitalize(), surename.capitalize())
    print("Age :", age, "years old")
    print("Occupation :", job.upper())
    print("=" * 6)
main()
