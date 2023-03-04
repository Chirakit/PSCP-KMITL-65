"""TheFunctionWithin"""

def input_any():
    """_"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    do_it(num1, num2, num3, num4)
def f_x(var):
    """f(x)"""
    total = 2 * var
    return total
def g_x(yar):
    """g(x)"""
    total = (3 * (yar ** 4)) - (yar ** 3) + (2 * (yar ** 2)) + 10
    return total
def h_xyz(xar, lar, zar):
    """h(x,y,z)"""
    total = ((zar + xar) ** 2) - (xar * lar) + (lar ** 2)
    return total
def i_abcd(aar, oar, car, dar):
    """i(a,b,c,d)"""
    total = ((aar**2)+(oar**2)-(car**2))/((dar**2)-(2*(aar*dar))+(2*aar))
    return total
def do_it(sum1, sum2, sum3, sum4):
    """_"""
    print(f_x(f_x(sum1)))
    print(g_x(f_x(sum1 - sum2)))
    print(h_xyz(f_x(sum1 + sum2), f_x(sum1 + sum3), g_x(f_x(sum4 ** 2))))
    print(i_abcd(h_xyz(f_x(sum1 + sum2), f_x(sum1 - sum3), g_x(f_x(sum4 ** 2))),\
g_x(f_x(sum1 - sum2)), f_x(f_x(f_x(f_x(f_x(sum3))))), sum4 ** 8))

input_any()
