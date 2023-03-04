""" เลือกคนคุยให้หน่อย """
def main():
    """ That too many of em """
    trait_1 = input()
    trait_2 = input()
    if trait_1 == "Calm" and trait_2 == "Empathetic" \
        or trait_1 == "Empathetic" and trait_2 == "Calm":
        print("Ice")
    elif trait_1 == "Reliable" and trait_2 == "Courageous" \
        or trait_1 == "Courageous" and trait_2 == "Reliable":
        print("Fern")
    elif trait_1 == "Optimistic" and trait_2 == "Cheerful" \
        or trait_1 == "Cheerful" and trait_2 == "Optimistic":
        print("Bam")
    elif trait_1 == "Attractive" and trait_2 == "Creative" \
        or trait_1 == "Creative" and trait_2 == "Attractive":
        print("Tangmo")
    elif trait_1 == "Cheerful" and trait_2 == "Creative" \
        or trait_1 == "Creative" and trait_2 == "Cheerful":
        print("Mild")
    elif trait_1 == "Reliable" and trait_2 == "Optimistic" \
        or trait_1 == "Optimistic" and trait_2 == "Reliable":
        print("Prae")
    elif trait_1 == "Courageous" and trait_2 == "Calm" \
        or trait_1 == "Calm" and trait_2 == "Courageous":
        print("Dream")
    elif trait_1 == "Empathetic" and trait_2 == "Attractive" \
        or trait_1 == "Attractive" and trait_2 == "Empathetic":
        print("Aom")
main()
