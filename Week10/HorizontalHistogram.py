'''HorizontalHistogram'''
def sort_value(var):
    """_"""
    char = var[0]
    return ord(char) + (100 if char.isupper() else 0)

def main(string):
    """_"""
    for char, count in sorted({i: string.count(i) for i in string}.items(), key=sort_value):
        print(char, ":", "".join(["-" if i % 5 else "-|" for i in range(1, count+1)]).rstrip("|"))

main(input())
