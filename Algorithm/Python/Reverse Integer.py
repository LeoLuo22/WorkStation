def reverse(x):
    x1 = int(str(x).replace("-","")[::-1])
    if (x1 > -2147483648 and x1 < 2147483647 ):
        return x1 if x > 0 else -x1
    return 0
print(reverse(1534236469))
