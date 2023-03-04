""" Temperature """
def main():
    """ input here """
    num_0 = float(input())
    temp = input()
    if temp == "C→F":
        cel_to_fahr(num_0)
    elif temp == "C→K":
        cel_to_kel(num_0)
    elif temp == "C→R":
        cel_to_ran(num_0)
    elif temp == "F→C":
        fahr_to_cel(num_0)
    elif temp == "F→K":
        fahr_to_kel(num_0)
    elif temp == "F→R":
        fahr_to_ran(num_0)
    elif temp == "K→C":
        kel_to_cel(num_0)
    elif temp == "K→F":
        kel_to_fahr(num_0)
    elif temp == "K→R":
        kel_to_ran(num_0)
    elif temp == "R→C":
        ran_to_cel(num_0)
    elif temp == "R→F":
        ran_to_fahr(num_0)
    elif temp == "R→K":
        ran_to_kel(num_0)
def cel_to_fahr(cel):
    """ convert cel_to_fahr """
    fahr = (cel * 9/5) + 32
    print("Fahrenheit = %.2f"%fahr)
def cel_to_kel(cel):
    """ convert cel_to_kel """
    kel = cel + 273.15
    print("Kelvin = %.2f"%kel)
def cel_to_ran(cel):
    """ convert cel_to_ran """
    ran = (cel * 9/5) + 273.15
    print("Rankine = %.2f"%ran)
def fahr_to_cel(fahr):
    """ convert fahr_to_cel """
    cel = (fahr - 32) * 5/9
    print("Celsius = %.2f"%cel)
def fahr_to_kel(fahr):
    """ convert fahr_to_kel """
    kel = (fahr + 459.67) * 5/9
    print("Kelvin = %.2f"%kel)
def fahr_to_ran(fahr):
    """ convert fahr_to_ran """
    ran = fahr + 459.67
    print("Rankine = %.2f"%ran)
def kel_to_cel(kel):
    """ convert kel_to_cel """
    cel = kel - 273.15
    print("Celsius = %.2f"%cel)
def kel_to_fahr(kel):
    """ convert kel_to_fahr """
    fahr = (kel * 9/5) - 459.67
    print("Fahrenheit = %.2f"%fahr)
def kel_to_ran(kel):
    """ convert kel_to_ran """
    ran = kel * 9/5
    print("Rankine = %.2f"%ran)
def ran_to_cel(ran):
    """ convert ran_to_cel """
    cel = (ran * 5/9) - 491.67
    print("Celsius = %.2f"%cel)
def ran_to_fahr(ran):
    """ convert ran_to_fahr """
    fahr = ran - 491.67
    print("Fahrenheit = %.2f"%fahr)
def ran_to_kel(ran):
    """ convert ran_to_kel """
    kel = ran * 5/9
    print("Kelvin = %.2f"%kel)
main()
