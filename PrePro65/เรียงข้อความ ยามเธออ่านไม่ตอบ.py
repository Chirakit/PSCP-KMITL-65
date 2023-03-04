""" เรียงข้อความ ยามเธออ่านไม่ตอบ """
def main():
    """ ปกติเธอก็อ่านไม่ตอบอยู่แล้ว """
    text_1 = input().capitalize()
    text_2 = input().capitalize()
    text_3 = input().capitalize()
    oop_1 = len(text_1)
    oop_2 = len(text_2)
    oop_3 = len(text_3)
    if oop_1 < oop_2 < oop_3:
        print(text_1)
        print(text_2)
        print(text_3)
    elif oop_1 < oop_3 < oop_2:
        print(text_1)
        print(text_3)
        print(text_2)
    elif oop_2 < oop_1 < oop_3:
        print(text_2)
        print(text_1)
        print(text_3)
    elif oop_2 < oop_3 < oop_1:
        print(text_2)
        print(text_3)
        print(text_1)
    elif oop_3 < oop_1 < oop_2:
        print(text_3)
        print(text_1)
        print(text_2)
    elif oop_3 < oop_2 < oop_1:
        print(text_3)
        print(text_2)
        print(text_1)
main()
