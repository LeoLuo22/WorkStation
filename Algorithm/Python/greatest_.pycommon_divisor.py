a = int(input("a:"))
b = int(input("b:"))
#辗转相除法
"""
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
"""
def gcd(a, b):
    count = 0
    while True:
        if a % 2 == 0 and b % 2 == 0:
            a, b = a // 2, b // 2
            count += 1
        else:
            break
    while True:
        if a < b:
            a, b = b, a
        c = a - b
        if c == b:
            return (c * 2 ** count if count else c)
        a, b = b, c


print(gcd(a,b))
