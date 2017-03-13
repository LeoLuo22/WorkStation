def f(s):
    s = s.split()
    if len(s) <= 0:
        return 0
    return len(s[len(s)-1])

print(f("he world"))
