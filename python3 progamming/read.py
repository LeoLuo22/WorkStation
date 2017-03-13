item = open('test1.lst',encoding='utf-8')
"""
for line in item:
    print(line)
"""
try:
    all_item = item.read()
    print(all_item)
finally:
    item.close()
