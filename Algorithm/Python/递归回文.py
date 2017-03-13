def find(to_find, n, i):
    if n <= len(to_find) // 2:
        return True
    try:
        if to_find[i] == to_find[n-1]:
            return find(to_find, n-1, i+1)
    except IndexError as err:
        print(i, " ", n-1)
    else:
        return False

print(find("sasdfdsas", len("sasdfdsas"), 0))
