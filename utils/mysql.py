"""Simplify pymysql
"""
import pymysql

class MySql():
    def __init__(self, db, user, passwd,
                 host='127.0.0.1', port=3306,
                 charset='utf8mb4',
                 cursorclass=pymysql.cursors.DictCursor,
                 collection=None):
        """连接到一个数据库
            @param db->数据库名
            @param user->用户名
            @param passwd->密码
            @param collection->默认要使用的集合名（表名）
        """
        self.config = {'db':db, 'user':user,
                       'password':passwd, 'host':host,
                       'port':port, 'charset':charset,
                       'cursorclass':cursorclass}
        self.connection = pymysql.connect(**self.config)
        self.collection = collection

    def find(self, collection=None, mohu=False, **kwargs):
        """查询一个记录，用法get({'city':'北京'})
            @param mohu->模糊查询
            @param **kwargs->字典
            @param collection->要查询的表，默认为初始化值
            @return None或者整条记录值
        """
        #print(kwargs)
        if collection is None:
            collection = self.collection

        #print(collection)
        key = ''
        for k in kwargs.keys():
            key = k
        value = kwargs.get(key)

        with self.connection.cursor() as cursor:
            if not mohu:
                sql = 'SELECT * FROM {0} WHERE {1}="{2}"'.format(collection, key, value)
            else:
                sql = 'SELECT * FROM {0} WHERE {1} like "{2}"'.format(collection, key, value)
            #print(sql)
            cursor.execute(sql)
            result = cursor.fetchone()
            self.connection.commit()

        return result

    def close(self):
        self.connection.close()
