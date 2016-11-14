# -*- coding:utf-8 -*-
__author__ = "Luo Hao"

import requests
import urllib
import http.cookiejar
from PIL import Image
from bs4 import BeautifulSoup
import lxml
import pytesseract
import re
import collections
import time
from io import StringIO

init_page = "http://wiscom.chd.edu.cn:8080/reader/login.php"
captcha_url = "http://wiscom.chd.edu.cn:8080/reader/captcha.php"
redr_verify = "http://wiscom.chd.edu.cn:8080/reader/redr_verify.php" #POST
redr_infp = "http://wiscom.chd.edu.cn:8080/reader/redr_info.php"#GET
book_lst = "http://wiscom.chd.edu.cn:8080/reader/book_lst.php"#GET
continue_borrow_url = "http://wiscom.chd.edu.cn:8080/reader/ajax_renew.php?" #GET
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
                        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Accept-Encoding':'gzip, deflate, sdch',
                        'Accept-Language':'zh-CN,zh;q=0.8',
                        'Cache-Control':'no-cache',
                        'Connection':'keep-alive',
                        'Host':'wiscom.chd.edu.cn:8080',
                        'Pragma':'no-cache',
                        'Referer':'http://portal.chd.edu.cn/',
                        'Upgrade-Insecure-Requests':'1'}

session = requests.Session()
session.get(init_page)

class InputError(Exception):pass

class Chdlib:
    def __init__(self, username=None, password=None, captcha=None, name=None, book_info_dict=None, cookie=None):
        self.__username = username
        self.__password = password
        self.__captcha = captcha
        self.__post_data = {'number':str(self.__username),
                                           'passwd':str(self.__password),
                                           'captcha':str(self.__captcha),
                                           'select':'cert_no'
        }
        self.__name = name
        self.__book_info_dict = book_info_dict#A dict saves the bar_code and check code of a book which are be used to post data in the "续借" url

    @property
    def book_info_dict(self):
        return self.__book_info_dict

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def captcha(self):
        return self.__captcha

    @captcha.setter
    def captcha(self, value):
        self.__captcha = value

    @property
    def name(self):
        return self.__name

    def get_captcha(self):
        """*****************Use Urllib and http.cookiejar************************
        cj = http.cookiejar.LWPCookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)
        req = urllib.request.Request("http://wiscom.chd.edu.cn:8080/reader/captcha.php")
        print("captcha: {0}".format(cj))
        self.__cookie = cj
        operate = opener.open(req)
        msg = operate.read()
        """
        """***************************use requests********************************"""
        r = session.get("http://wiscom.chd.edu.cn:8080/reader/captcha.php")
        with open('captcha.gif', 'wb') as fd:
                fd.write(r.content)
        """
        file_object = open('captcha.gif','wb')
        try:
            file_object.write(msg)
        finally:
            file_object.close()
        """
        #im = Image.open('captcha.gif')
        #im.show()
        code = pytesseract.image_to_string(Image.open('captcha.gif'))
        return code


    def login(self):
        """
        postdata = urllib.parse.urlencode(self.__post_data)
        postdata = postdata.encode('utf-8')
        """"""
        res = urllib.request.urlopen(redr_verify,postdata)
        """
        res = session.post(redr_verify, data=self.__post_data)
        if(res.status_code == 200):
            print("登陆成功")
        return res.content.decode('utf-8')

    def book_lst(self):
        """
        book_lst_page = urllib.request.urlopen(book_lst)
        return book_lst_page.read()
        """
        book_lst_page = session.get(book_lst)
        return book_lst_page.text

    def continue_borrow(self, captcha, seq_num=None):
        get_data = collections.OrderedDict()
        if seq_num == None:
            for i in range(0,len(self.__book_info_dict)):
                get_data['bar_code'] = self.__book_info_dict[i][2]
                get_data["check"] = self.__book_info_dict[i][3]
                get_data["captcha"] = str(captcha)
                get_data["time"] = str(int(round(time.time() * 1000)))
                r = session.get(continue_borrow_url, params=get_data)
                continue_borrow_soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')
                print("{0}  {1}".format(self.__book_info_dict[i][0],continue_borrow_soup.font.string))
                get_data = collections.OrderedDict()
        else:
            get_data['bar_code'] = self.__book_info_dict[seq_num][2]
            get_data["check"] = self.__book_info_dict[seq_num][3]
            get_data["captcha"] = str(captcha)
            get_data["time"] = str(int(round(time.time() * 1000)))
            print(str(int(round(time.time() * 1000))), len(str(int(round(time.time() * 1000)))))
            url = continue_borrow_url +  "bar_code=" +self.__book_info_dict[seq_num][2] + "&check=" + self.__book_info_dict[seq_num][3] + "&captcha=" + str(captcha) + "&time=" + str(int(round(time.time() * 1000)))
            """
        cj = http.cookiejar.LWPCookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)
        req = urllib.request.Request(url,method='GET')
        operate = opener.open(req)
        print(operate.read())
        #print(r.read())
        """
            r =session.get(url)
            continue_borrow_soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')
            print(print("{0}  {1}".format(self.__book_info_dict[seq_num][0],continue_borrow_soup.font.string)))


    def parse(self):
        """*************************获取用户名*******************************"""
        response = self.login()
        soup = BeautifulSoup(response, 'lxml')
        soup =soup.find('div',attrs={'id':'mylib_info'}).find('span', attrs={'class':'bluetext'}).find_parent()
        name = soup
        soup.span.decompose()
        self.__name = name.string
        """*************************获取当前借阅图书及其规划日期****************************"""
        self.__book_info_dict = collections.OrderedDict()
        book_page_responese  = self.book_lst()
        book_page_soup = BeautifulSoup(book_page_responese, 'lxml')
        books = book_page_soup.find_all('td',attrs={'class':'whitetext', 'width':'35%'})
        return_date = book_page_soup.find_all('td', attrs={'class':'whitetext', 'width':'13%'})
        tag_lst = []
        date_lst = []
        return_date_lst = []
        for tag in books:
            tag = tag.get_text()
            tag_lst.append(tag)
        for date in return_date:
            date = date.get_text()
            date_lst.append(date)
        for i in range(1,len(date_lst), 3):
            return_date_lst.append(date_lst[i])
        tmp = []
        for i in range(0,len(tag_lst)):
            tmp.append(tag_lst[i])
            tmp.append(return_date_lst[i])
            self.__book_info_dict[i] = tmp
            tmp = []
        """*************************获取已借阅书籍的bar_code和check**************************"""
        """*******************************并对应的存在list里***************************************"""
        bar_code = []
        check = []
        test = []
        book_info_tmp = []
        book_info = []
        bar_code_soup = book_page_soup.find_all('input',attrs={'title':'renew'})
        for item in bar_code_soup:
            test.append(item['onclick'])#re
        bar_code_re = "\\d{7}"
        r = re.compile(bar_code_re)
        for t in test:
            bar_code.append(re.search(r, t).group())
        check_re = "(\\d|A|B|C|D|E|F){8}"
        c_r = re.compile(check_re)
        for t in test:
            check.append(re.search(c_r, t).group())
        for i in range(0,len(check)):
            self.__book_info_dict[i].append(bar_code[i])
            self.__book_info_dict[i].append(check[i])
        for key, value in self.__book_info_dict.items():
            print(key, value)

def get_input(msg,  _type, username=None):
    if _type == 'username':
        while  True:
            username = input(msg)
            if len(username) != 12 or  not username.isdigit():
                print("输入有误， 请重新输入")
                continue
            break
        return username

    elif _type == "password":
        password = input(msg)
        if len(password) == 0:
            password = username
            return password
        else:
            return password
    elif _type == "seq_num":
        while True:
            seq_num = input(msg)
            if len(seq_num) == 0:
                return None
            seq_num = int(seq_num)
            if seq_num not in range(0,5):
                print("输入有误")
                continue
            break
        return seq_num

def main():
    user = Chdlib()
    username = get_input("输入你的学号: ", 'username')
    password = get_input("请输入密码，默认为学号（按回车键）: ", 'password', username)
    captcha = user.get_captcha()
    user = Chdlib(username, password, captcha)
    user.login()
    user.parse()
    print("欢迎，{0}".format(user.name))
    print("你当前所借阅的图书共{0}本".format(len(user.book_info_dict)))
    for key, value in user.book_info_dict.items():
        print("")
        print("{0}  {1}            归还日期: {2}".format(key, value[0], value[1]))
    captcha = user.get_captcha()
    seq_num = get_input("请输入要续借的序号，默认全部续借(按回车): ", "seq_num")
    user.continue_borrow(captcha, seq_num)

if __name__ == "__main__":
    main()



