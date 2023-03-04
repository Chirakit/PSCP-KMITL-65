"""BreakPassword"""
from hashlib import sha512
def main(d_hash):
    """hashing but backward"""
    for i in range(0, 100000):
        if hashin(str(i).zfill(5)) == d_hash:
            print(str(i).zfill(5))
            break

def hashin(num):
    """hash"""
    return sha512(num.encode("utf-8")).hexdigest().upper()

main(input())
