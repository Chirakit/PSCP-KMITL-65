""" Append """
import json
def main():
    """ add it """
    num_0 = int(input())
    text_mas = [input() for _ in range(num_0)]
    print(json.dumps(text_mas))
main()
