def sort(nums):
    bitmap = []
    rst= []
    for i in range(0, 27):
        bitmap.append(0)
    for num in nums:
        bitmap[num] = 1
    for i in range(0, 27):
        if bitmap[i] == 1:
            rst.append(i)
    return rst
print(sort([2, 3, 5, 8, 1, 4, 6]))
