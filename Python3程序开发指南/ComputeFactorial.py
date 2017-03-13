def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    while  True:
        n = int(input("input"))
        print(2 ** n)

main()
