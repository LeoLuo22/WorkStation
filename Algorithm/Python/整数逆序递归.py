def convert(result, n):
    if n > 10:
        convert(result, n // 10)
    result.append(n%10)
result = []
convert(result, 123456789)
for i in range((len(result)-1), -1, -1):
    print(result[i], end="")
