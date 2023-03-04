'''LetterFrequency'''
import string
def main():
    '''_'''
    txt = input().lower().replace(" ", "")
    value = list(filter(lambda a: a in string.ascii_letters, txt))
    value = max(set(txt), key=txt.count)
    print(value)

main()
