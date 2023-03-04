""" ร้านขายเสื้อของจอมเวทย์ """
def main():
    """ What the heck is this? """
    role = input()
    armor = 12800
    if role != "Magician":
        ea_1 = int(input())
        print("Total %d Jewel"%(armor * ea_1))
    elif role == "Magician":
        guild = input()
        ea_1 = int(input())
        if guild == "Fairy Tail":
            discount = ((armor * ea_1) * 20 / 100)
            total = (armor * ea_1) - discount
            print("Total %d Jewel"%total)
        elif guild == "Sabertooth" and ea_1 > 5:
            discount = ((armor * ea_1) * 15 / 100)
            total = (armor * ea_1) - discount
            print("Total %d Jewel"%total)
            if ea_1 <= 5:
                print("Total %d Jewel"%(armor * ea_1))
        elif guild == "Lamia Scale" and ea_1 >= 3:
            discount = ((armor * ea_1) * 10 / 100)
            total = (armor * ea_1) - discount
            print("Total %d Jewel"%total)
            if ea_1 < 3:
                print("Total %d Jewel"%(armor * ea_1))
        elif guild == "Blue Pegasus" and ea_1 > 10:
            discount = ((armor * ea_1) * 5 / 100)
            total = (armor * ea_1) - discount
            print("Total %d Jewel"%total)
            if ea_1 <= 10:
                print("Total %d Jewel"%(armor * ea_1))
        else:
            print("Total %d Jewel"%(armor * ea_1))
main()
