"""获取每个省份的互联网公司数目
"""
from utils.mongo import connect

counter = {}
cursor = connect('lagou', 'location')

for result in cursor.find():
    nums = result.get('company_nums')
    province = result.get('province')

    if province not in counter.keys():
        counter[province] = nums
    else:
        counter[province] = counter.get(province)+nums

for key, value in counter.items():
    print('{name:', "'",key,"'", ',', 'value:', value, '},')
