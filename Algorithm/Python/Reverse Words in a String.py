def reverseWords(s):
    strings = s.split()[::-1]
    result = ""
    for string in strings:
        if strings.index(string) != len(strings) - 1:
            string += " "
        result += string
    return result
print(len(reverseWords("A b c")))
