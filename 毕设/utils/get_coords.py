"""从百度地图api获得坐标
并写入到mongodb
"""
import pymongo
import requests
import json
from urllib import parse

def connect(db, collection):
    """创建连接
        @param db
         数据库名
        @param collection
         集合名
        @return
         返回游标
    """
    client = pymongo.MongoClient('127.0.0.1')
    db = client[db]
    cursor = db[collection]

    return cursor

def get_coord(ak, address, city=None, output=None):
    """获取坐标
        @param ak
         用户的key
        @param address
         详细地址
        @city
         城市
        @output
         返回格式,默认为xml
    """
    service = 'http://api.map.baidu.com/geocoder/v2/'

    payload = {'ak': ak, 'address': address,
               'city': city, 'output': output}

    response = requests.get(service, params=payload)

    return json.loads(response.text)

def main():
    exists = set()

    cursor = connect('lagou', 'location')
    results = cursor.find()

    new_cursor = connect('location', 'china')

    exists_ = new_cursor.find()

    for exist in exists_:
        city = exist.get('city')
        exists.add(city)

    for result in results:
        tmp = {}
        address = result.get('city')

        if address in exists:
            continue

        tmp['city'] = address

        if not address:
            continue

        response = get_coord('AlZIqiZ4qaVTkZG0VokCnRYNIjzoqcfB', address, output='json')
        try:
            tmp['location'] = response.get('result').get('location')
        except AttributeError:
            print(address)
            return

        new_cursor.insert(tmp)

if __name__ == '__main__':
    main()
