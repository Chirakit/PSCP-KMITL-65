'''Password'''
from hashlib import sha512
def main():
    """hash"""
    num = input().encode("utf-8")
    print(sha512(num).hexdigest().upper())
main()
