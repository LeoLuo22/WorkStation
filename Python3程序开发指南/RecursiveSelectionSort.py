def sort(lst):
    sortHelper(lst, 0, len(lst) - 1)

def sortHelper(lst, low, high):
    if low < high:
        index_of_min = low
        try:
            min = lst[low]
        except IndexError as err:
            print(low)
        for i in range(low + 1, high + 1):
            try:
                if lst[i] < min:
                    min = lst[i]
                    index_of_min = i
                    break
            except IndexError as err:
                print(i)
        try:
            lst[index_of_min] = lst[low]
            lst[low] = min
        except IndexError as err:
            print(index_of_min)
        sortHelper(lst, low + 1, high + 1)

def main():
    lst = [3, 2, 1, 5, 9 ,0]
    print(sort(lst))

main()
