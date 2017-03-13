#-*-coding:utf-8-*-
__author__ = "Leo Luo"

def insertion_sort(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        j = i - 1
        while j >= 0 and seq[j] > key:
            seq[j + 1] = seq[j]
            seq[j] = key
            j -= 1


def main():
    seq = []
    while True:
        value = input("Please input value: ")
        if len(value) == 0:
            break
        seq.append(int(value))
    insertion_sort(seq)
    print(seq)

if __name__ == "__main__":
    main()



