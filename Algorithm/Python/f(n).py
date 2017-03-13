#-*-coding:utf-8-*-
__author__ = "Leo Luo"

def f(n):
    count = 0
    for i in range(1, n+1):
        i = str(i)
        for j in i:
            if j == "1":
                count += 1
    return count

def what_n(n):
    return (True if n == f(n) else False)

def main():
    n = int(input("n: "))
    print(what_n(n))

if __name__ == "__main__":
    main()
