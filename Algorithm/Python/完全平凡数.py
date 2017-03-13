def havesamenum(n):
    if n < 10:
        return False
    tmp = []
    count = 0
    while n > 0:
        r = n % 10
        tmp.append(r)
        n = n // 10
    for i in range(0, len(tmp)):
        for j in range(i, len(tmp)):
            if tmp[i] == tmp[j] and i != j:
                #print(tmp[i], " ", tmp[j])
                return True
    return False

for i in range(1, 100):
    x = i ** 2
    if havesamenum(x):
        print(x)
