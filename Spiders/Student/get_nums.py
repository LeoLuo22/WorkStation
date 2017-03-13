import xlrd

file = xlrd.open_workbook("F://2012.xls")
table = file.sheet_by_index(0)
count = 0
for value in table.col_values(7):
    value += "\n"
    count += 1
    with open("2012.txt", "a") as fh:
        fh.write(value)
print(count)
