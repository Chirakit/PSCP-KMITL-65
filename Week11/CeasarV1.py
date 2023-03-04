"""CaesarV1"""
def main():
    """CaesarV1"""
    import string
    a_z = string.ascii_lowercase
    step = int(input())
    text = input()
    result = ""
    for i in text:
        if i.islower():
            idx = a_z.find(i)
            result += a_z[(idx+step)%26]
        elif i.isupper():
            idx = a_z.upper().find(i)
            result += a_z.upper()[(idx+step)%26]
        else:
            result += i
    print(result)
main()
