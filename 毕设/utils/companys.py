"""获取公司的ID
    写入到数据库
"""
from utils import mongo

cursor = mongo.connect('lagou', 'jobs')

results = cursor.find()
companys = set()

for result in results:
    companyId = result.get('companyId')
    companys.add(companyId)

print(len(companys))

c = mongo.connect('lagou', 'companys')
for company in companys:
    item = {}
    item['companyId'] = company
    c.insert(item)
