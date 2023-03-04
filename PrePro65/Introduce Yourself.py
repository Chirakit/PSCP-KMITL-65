""" Introduce Yourself """
def main():
    """ Input name(str) nickname(str) age(int) """
    name = str(input())
    nickname = str(input())
    age = int(input())
    year = 2022 - age
    print("My name is %s, My nickname is %s, I'm I was born in %d"%(name, nickname, year))
main()
