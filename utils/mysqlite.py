"""用来简化sqlite操作"""
import sqlite3

class MySqlite():
    def __init__(self, dbpath, table=None):
        """创建数据库连接
            @param dbpath
             数据库文件所在路径
            @param table
             要连接的表名，默认为空
        """
        self.connection = sqlite3.connect(dbpath)
        self.cursor = self.connection.cursor()
        self.table = table

    def __dict_factory(self, row):
        """将sqlite3查询的返回值转成字典的形式
            @param row
             查询的结果集
        """
        return dict((col[0], row[idx]) for idx, col in enumerate(self.cursor.description))

    def newtable(self, table, **kwargs):
        """创建表
            @param table
             表名
            @param kwargs
             关键字参数
            Usage:
            ('test', _id='varchar(20)', username='vachar(20)')
        """
        sql = "create table " + table + " ({0})"
        args = ""
        for key, value in kwargs.items():
            tmp = key + ' ' + value + ', '
            args += tmp
        #print(sql.format(args).replace(', )', ')'))
        self.connection.execute(sql.format(args).replace(', )', ')'))
        self.connection.commit()

    def create(self, table=None, **kwargs):
        """向表中插入数据
            @param kwargs
             要插入的数据
            @param table
             表名，如果连接了的话不用填
             Usage:
             sqlite.create('test', _id='1', username='Leo', password='mm123456')
        """
        if not table and not self.table:
            raise ValueError("未指定连接到表")
        elif table:
            table = table
        else:
            table = self.table

        k = ""
        v = ""
        for key, value in kwargs.items():
            key += ', '
            value = '\'' + value + '\'' + ', '
            k += key
            v += value
        sql = "insert into " + table + " ({0}) values ({1})".format(k[:-2], v[:-2])
        #print(sql)
        self.cursor.execute(sql)
        self.connection.commit()

    def find_one(self, table=None, **kwargs):
        """查询一条记录
            @param table
             无默认则必须指定
            @param kwargs
             查询条件
        """
        if not table and not self.table:
            raise ValueError("未指定连接到表")
        elif table:
            table = table
        else:
            table = self.table

        sql = "select * from " + table + " where {0}='{1}'"
        k = ""
        v = ""
        for key, value in kwargs.items():
            k = key
            v = value
        sql = sql.format(k, v)
        #print(sql)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result is None:
            return None
        return self.__dict_factory(result)
    """
    def find(self, table=None):
        sql =
    """
    def close(self):
        #关闭数据库连接
        self.cursor.close()
        self.connection.close()

def main():
    sqlite = MySqlite('F:/test.db', 'users')
    #sqlite.newtable('user', _id='varchar(20) primary key', name='varchar(20)', password='varchar(20)')
    #sqlite.create('user', _id='1', name='Leo', password='mm123456')
    print(sqlite.find_one(name='Leo'))
    sqlite.close()

if __name__ == '__main__':
    main()
