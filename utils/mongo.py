"""简化了一些mongo的操作
   connect(db, collection)
   @author: Leo Luo
"""
import pymongo

def connect(db, collection, host=None, port=None):
    """连接到一个集合
        @param db
         数据库名
        @param collection
         集合名
        @param host
         地址。默认为127.0.0.1
        @param port
         端口。默认为27017
        @return
         A cursor.
    """
    if not host:
        host = '127.0.0.1'
    if not port:
        port = 27017

    client = pymongo.MongoClient(host, port)
    db = client[db]
    cursor = db[collection]

    return cursor
