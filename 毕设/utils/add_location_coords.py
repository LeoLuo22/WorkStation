"""添加各个城市的坐标到数据库
"""
import pymongo
import collections

client = pymongo.MongoClient('127.0.0.1')
#db = client.location

#results = db.china.find()

#geos = {}

#先经后纬
"""
for result in results:
    tmp = []
    location = result.get('location')
    tmp.append(location.get('lng'))
    tmp.append(location.get('lat'))
    geos[result.get('city')] = tmp
print(geos)
"""
db = client.lagou
results = db.location.find()
for result in results:
    tmp = {}
    tmp['name'] = result.get('city')
    tmp['value'] = result.get('company_nums')
    print(tmp,', ')

