"""统计各个分类下的人数
"""
from utils.mongo import connect

cursor = connect('lagou', 'categories')

counter = {}

for result in cursor.find():
    category = result.get('category')
    if category in counter.keys():
        counter[category] = counter.get(category) + 1
    else:
        counter[category] = 1

print(counter)
