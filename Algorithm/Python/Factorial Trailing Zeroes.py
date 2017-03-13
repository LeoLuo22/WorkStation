def count(n):
    f = 1
    count = 0
    for i in range(1, n+1):
        f *= i
    print(f)
    f = str(f)
    flag = '0'
    for j in range(len(f)-1, -1, -1):
        if f[j] == '0':
            count += 1
        else:
            break
    return count

print(count(4838))
