'''MissingCard I'''
def main():
    '''_'''
    txt = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    card = []
    for i in txt:
        card_s = i + "S"
        card_h = i + "H"
        card_d = i + "D"
        card_c = i + "C"
        card.append(card_s)
        card.append(card_h)
        card.append(card_d)
        card.append(card_c)
    for _ in range(51):
        missing_card = str(input())
        if missing_card in card:
            card.remove(missing_card)
    print(card[0])

main()
