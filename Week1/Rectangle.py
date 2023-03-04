"""Rectangle"""
def minecraft():
    """_"""
    heigh = int(input())
    widge = int(input())
    total(heigh, widge)

def total(heigh, widge):
    """_"""
    area = heigh * widge
    around = (heigh + widge) * 2
    print(area, around, sep="\n")
minecraft()
