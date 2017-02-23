"""This module is to provide proxies
"""
import requests
import pymysql
from utils import user_agents
import random
from bs4 import BeautifulSoup
from datetime import datetime
import lxml

class MySql(object):
    def __init__(self,  user=None, passwd=None, db=None, host='127.0.0.1', port=3306):
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
        'user': 'Leo',
        'password': 'mm123456',
        'db': 'utils',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
        }

        #self.proxies = []
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
        #self.__close()

        return results

    def update(self, host, available):
        """Update data to database
        """
        sql = "UPDATE proxies SET available = '{available}' , lastcheck = '{datetime}' WHERE host = '{host}'".format(available=available, host=host, datetime=datetime.now())

        self.cursor.execute(sql)
        self.connection.commit()
        #self.__close()

    def check_for_update(self):
        """Check all proxy if it is available
           And write them to database
        """
        proxies = self.retrieve('host', 'protocol', 'port')
        for proxy in proxies:
            if wash(**proxy):
                self.update(proxy.get('host'), 1)
            else:
                self.update(proxy.get('host'), 0)

    def __close(self):
        self.cursor.close()
        self.connection.close()

def wash(protocol=None, host=None, port=None):
    """Test if it can connect to Bing
    """
    proxy = {}
    url = protocol + '://' + host + ':' + port
    proxy[protocol] = url
    print('Testing ', url, end='')
    #print(' ', proxy, end='')
    header = {}
    header['User-Agent'] = random.choice(user_agents.UserAgents)
    #print(header)
    try:
        response = requests.get('http://1212.ip138.com/ic.asp', headers=header, timeout=1, proxies=proxy)
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError,
            requests.exceptions.ReadTimeout, requests.exceptions.ChunkedEncodingError):
        print('    error occured')
        return False
    #print(response.text)
    soup = BeautifulSoup(response.content, 'lxml')
    #div = soup.find('body', attrs={'style': 'margin:0px'})

    #获取网页上显示的IP
    try:
        ip = soup.find('center').get_text().split('[')[1].split(']')[0]
    except AttributeError:
        print('    error occured')
        return False
    print('    Showed IP: ', ip, end='')
    if host == ip:
        print('......ok')
        return True
    print('......fail')
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
def get_avaiables():
    """Get available proxies from database
    @return
     list, contains http://1.1.1.1:80
    """
    mysql = MySql()
    proxies = []
    proxy = ''
    results = mysql.retrieve('protocol', 'port', 'host', available=1)
    for result in results:
        proxy = result.get('protocol') + '://' + result.get('host') + ':' + result.get('port')
        proxies.append(proxy)

    return proxies

def get_http_from_xici(quantity=100):
    """Get http proxy from xici
    @param quantity
     Quantity of proxies, default is 100
    @return
     list, dict of proxy
    """
    mysql = MySql()
    my_proxies = mysql.retrieve('host', 'protocol', 'port')

    proxies = []
    base = 'http://www.xicidaili.com/wt/{0}'
    header = {}
    header['User-Agent'] = random.choice(user_agents.UserAgents)

    for i in range(1, 100):
        proxy = {}
        if len(proxies) <= 100:
            response = requests.get(base.format(i), headers=header)
            soup = BeautifulSoup(response.text, 'lxml')
            ip_list_soup = soup.find('table', attrs={'id': 'ip_list'})
            odds_soup = ip_list_soup.find_all('tr', attrs={'class': 'odd'})
            for odds in odds_soup:
                tds = odds.find_all('td')
                proxy['host'] = tds[1].get_text()
                proxy['port'] = tds[2].get_text()
                proxy['protocol'] = 'http'
                #print(proxy)
                if proxy not in my_proxies:#去重
                    proxies.append(proxy)
                proxy = {}

    return proxies

def get_xici_write(proxies):
    """Check if it is available and write to mysql
    @param get_http_from_xici
     function
    """
    mysql = MySql()
    for proxy in proxies:
        if wash(**proxy):
            mysql.create(**proxy, last_check=datetime.now(), available=1)
        else:
            mysql.create(**proxy, last_check=datetime.now(), available=0)

def main():
    mysql = MySql()
    #mysql.check_for_update()
    get_xici_write(get_http_from_xici(2000))

if __name__ == '__main__':
    main()
