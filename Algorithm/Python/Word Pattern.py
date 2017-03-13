def f(patterns, str):
    str_lst = str.split()
    if(len(patterns) != len(str_lst)):
        return False
    if len(set(str_lst)) != len(set(patterns)):
        return False
    d = {}
    for i in range(0, len(str_lst)):
        if patterns[i] in d.keys():
            if d[patterns[i]] != str_lst[i]:
                return False
        d[patterns[i]] = str_lst[i]
    return True
print(f("abba", "dog dog dog dog"))
