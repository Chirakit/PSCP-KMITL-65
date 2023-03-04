'''Filter'''
import json
def main():
    """Main function"""
    num = input()
    dis_1 = ['0']
    test = float(input())
    num = json.loads(num)
    for key in num:
        if num[key] >= test:
            dis_1.append('%s %.2f' %(key, float(num[key])))
        else:
            pass
    if len(dis_1) >= 2:
        dis_1.remove('0')
    dis_1.sort()
    for i in dis_1:
        if i == "0":
            print("Nope")
            break
        else:
            print("%s\t%.2f" %(i[0:8], float(i[9::])))

main()
