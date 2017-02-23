"""This module is to provide proxies
"""
import requests
import pymysql
from bs4 import BeautifulSoup
from datetime import datetime
import lxml
HEADER = {'User-Agent':
          'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

starturl = 'http://www.kuaidaili.com/free/inha/1/'

URLS = []

class MySql(object):
    def __init__(self,  user, passwd, db=None, host='127.0.0.1', port=3306):
        """Initialize a connection
        @param user
         username
        @param passwd
         password
        @param db
         database's name
        """
        self.config = {
        'host': host,
        'port': port,
        'user': user,
        'password': passwd,
        'db': 'utils',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
        }

        self.proxies = []
        self.connection = pymysql.connect(**self.config)
        self.cursor = self.connection.cursor()

    def create(self, protocol, host, port, last_check, available=0):
        """Insert into database
        @param protocol
         http or https
        @param host
         host
        @param port
         port
        @last_check
         datetime
        @available
         1->useful
        """
        try:
            sql = 'INSERT INTO proxies (protocol, host, port, available, lastcheck) VALUES (%s, %s, %s, %s, %s)'
            self.cursor.execute(sql, (protocol, host, port, available, last_check))
            self.connection.commit()
        except pymysql.err.IntegrityError as err:
            print(err)

    def retrieve(self, *args, **kwargs):
        """Get data from database
        """
        target = ''
        for arg in args:
            arg = arg + ', '
            target += arg
        target = target[0:len(target)-2]

        if kwargs.get('available') == 1:
            sql = 'SELECT {0} FROM proxies where available = 1'.format(target)
        else:
            sql = 'SELECT {0} FROM proxies'.format(target)

        try:
            self.cursor.execute(sql)
        except pymysql.err.InternalError as err:
            print('错误: ',err)
            return
        results = self.cursor.fetchall()
        self.connection.commit()

        proxy = []
        for result in results:
            proxy = result.get('protocol') + '://' + result.get('host') + ':' + result.get('port')
            self.proxies.append(proxy)

        self.__close()

    def update(self, host, available):
        """Update data to database
        """
        sql = "UPDATE proxies SET available = '{available}' , lastcheck = '{datetime}' WHERE host = '{host}'".format(available=available, host=host, datetime=datetime.now())
        self.cursor.execute(sql)
        self.connection.commit()
        self.__close()


    def __close(self):
        self.cursor.close()
        self.connection.close()

def getUrl():
    for i in range(1, 200):
        url = starturl.replace("1", str(i))
        r = requests.get(url, headers=HEADER)
        rst = wash(r.text)
        if rst:
            print(rst)
            with open('proxies.txt', 'a') as fh:
                fh.write(rst + '\n')
    return

def wash(urlRaw):
    ips = []
    ports = []
    urlSoup = BeautifulSoup(urlRaw, 'lxml')
    ipsRaw = urlSoup.find_all('td', attrs={'data-title': 'IP'})
    portsRaw = urlSoup.find_all('td', attrs={'data-title': 'PORT'})

    for i in range(len(ipsRaw)):
        url = "http://" + ipsRaw[i].get_text() + ":" + portsRaw[i].get_text()
        if test(url):
            return url
        return

def test(url):
    proxy = {'http': url}
    try:
        r = requests.get('https://www.baidu.com', proxies=proxy, headers=HEADER, timeout=2)
    except Exception:
        return False
    if r.status_code == 200:
        return True
    return False

def addr_split(addr):
    """Spilt address like https://106.46.136.27:808
    @param addr
     Proxy address
    @return
     dict, {'protocol': '', 'host', 'port':}
    """
    if addr.startswith('h'):
        first_split = addr.split('//')
        protocol, second_split = first_split[0].replace(':',''), first_split[1].split(':')
        host, port = second_split[0], second_split[1]
        return {'protocol': protocol, 'host': host, 'port': port}
    else:
        split = addr.split(':')
        host, port = split[0], split[1]
        return {'protocol': 'http', 'host': host, 'port': port}

def read_from_file(filename):
    """Read proxy like http://1.1.1.1:80 from file
    @param filename
     file's path
    """
    rst = []

    with open(filename, 'r') as filehandler:
        for line in filehandler:
            rst.append(line.replace('\n', ''))

    return rst

def main():
    mysql = MySql('Leo', 'mm123456')
    #mysql.retrieve('protocol', 'port', 'host', available=1)
    #print(mysql.proxies)
    mysql.update('106.46.136.27', 1)

    """
    with open('proxies.txt', 'r') as fh:
        for line in fh:
            print(line.replace('\n', ''))
    """
if __name__ == '__main__':
    main()
