"""统计公司与地点
    类似单词计数程序
    like {'city': 公司数}
"""
import pymongo

def main():
    client = pymongo.MongoClient('127.0.0.1')
    db = client.lagou
    collection = db.jobs

    companys = set()
    counter = {}
    items = collection.find()

    for item in items:
        companyId = item.get('companyId')
        location = item.get('location')

        if companyId in companys:
            continue

        companys.add(companyId)

        if location in counter.keys():
            counter[location] = counter.get(location) + 1
        else:
            counter[location] = 1

    print('Total companies: ', len(companys))
    print('各个地点的公司数目如下：')

    for key, value in counter.items():
        tmp = {}
        tmp['city'] = key.replace(' ', '')
        tmp['company_nums'] = value
        db.location.insert(tmp)
        print(key, ' : ', value)

if __name__ == '__main__':
    main()
