#-*-coding:utf-8-*-
import itertools

__author__ = "Leo Luo"

def vampire_num(n):
    v1 = ""
    v2 = ""
    str_n = str(n)
    lst = []
    flag = len(str_n) // 2
    for i in itertools.permutations(str_n, len(str_n)):
        lst.append(i)
    for value in lst:
        for i in range(0, flag):
            v1 += value[i]
            v2 += value[flag+i]
        v1, v2 = int(v1), int(v2)
        if n == v1 * v2:
            print("{0} = {1} * {2}".format(n, v1, v2))
            return True
        v1, v2= "", ""
    return False

def main():
    for i in range(10, 99999999):
        vampire_num(i)

if __name__ == "__main__":
    main()

