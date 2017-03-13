#-*-coding:utf-8-*-
__author__ = "Leo Luo"

#把A上的n个盘子移动到C，可以用到B
def hanoi(A, B, C, n):
    if n == 1:
        print("Move disk {0} from {1} to {2}".format(n, A, C))
    else:
        hanoi(A, C, B, n - 1)
        print("Move disk {0} from {1} to {2}".format(n, A, C))
        hanoi(B, A, C, n - 1)

def main():
    n = int(input("Enter the value of Hanoi Tower: "))
    hanoi('A', 'B', 'C', n)

if __name__ == "__main__":
    main()

