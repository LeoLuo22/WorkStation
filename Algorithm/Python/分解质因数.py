def is_prime(n):
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find(n ,result):
    for i in range(2, n+1):
        if is_prime(i) and n % i == 0:
            result.append(i)
            return find(n // i, result)

result = []
n = int(input("n: "))
find(n, result)
print(result)

