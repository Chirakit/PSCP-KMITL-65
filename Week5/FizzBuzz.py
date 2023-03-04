"""FizzBuzz"""
def fizz():
    """_"""
    num = int(input())
    for i in range(num):
        lol = i + 1
        txt = lol
        if lol % 3 == 0 and lol % 5 == 0:
            lol = str(lol)
            txt = lol.replace(lol, "FizzBuzz")
        elif lol % 3 == 0:
            lol = str(lol)
            txt = lol.replace(lol, "Fizz")
        elif lol % 5 == 0:
            lol = str(lol)
            txt = lol.replace(lol, "Buzz")
        print(txt)
fizz()
