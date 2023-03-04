"""Flatten"""
def main():
    """Flatten"""
    import json
    text = json.loads(input())
    result = []
    while True:
        count = 0
        tmp = []
        if len(text) == 0:
            break
        for _ in range(len(text)):
            if isinstance(text[0+count], int):
                result.append(text[0+count])
                text.remove(text[0+count])
            else:
                count += 1
        for i in range(len(text)):
            tmp.extend(text[i])
        text = tmp
    print(sorted(result)[::-1])
main()
