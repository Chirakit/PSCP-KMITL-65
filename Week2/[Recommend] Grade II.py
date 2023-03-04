"""Grade II"""
def main():
    """_"""
    num = float(input())
    if num > 100 or num < 0:
        print("ERR")
    elif num >= 95:
        print("A")
    elif num >= 90:
        print("B+")
    elif num >= 85:
        print("B")
    elif num >= 80:
        print("C+")
    elif num >= 75:
        print("C")
    elif num >= 70:
        print("D+")
    elif num >= 65:
        print("D")
    elif num >= 60:
        print("F+")
    elif num >= 0:
        print("F")
main()
