""""[Recommend] Restaurant"""
def restaurant(current, promo, discount, offer):
    """_"""
    if current + offer >= promo:
        pay_with_offer = (current + offer) * (100-discount)/100
    else:
        pay_with_offer = current + offer
    if current >= promo:
        pay_without_offer = current * (100-discount)/100
    else:
        pay_without_offer = current
    diff = abs(pay_with_offer-pay_without_offer)
    if pay_with_offer < pay_without_offer:
        print("Yes %.3f" %diff)
    elif pay_with_offer > pay_without_offer:
        print("No %.3f" %diff)
    else:
        print("Yes")
restaurant(float(input()), float(input()), float(input()), float(input()))
