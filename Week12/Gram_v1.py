"""Ejudge"""
def main():
    """Gram-V.1"""
    txt = input()
    gramy = []
    for i in range(len(txt)-1):
        gramy.append(txt[i:i+2])
    cnt = []
    for letter in gramy:
        cnt.append(gramy.count(letter))
    print(gramy[cnt.index(max(cnt))]+"\n"+str(max(cnt)))
main()
