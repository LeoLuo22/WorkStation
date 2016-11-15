#-*- coding:utf-8 -*-
__author__ = "Leo Luo"

import requests
from bs4 import BeautifulSoup
import collections
import lxml
import os
from chd_lib import Chdlib
import Portal
import sys

BASE_URP_URL = "http://bksjw.chd.edu.cn"
LOGIN_URL = "http://bksjw.chd.edu.cn/loginAction.do"
HEAD = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0','Connection': 'Keep-Alive'}
IMG_URL = "http://bksjw.chd.edu.cn/xjInfoAction.do?oper=img" #头像的URL
USER_INFO_URL = "http://bksjw.chd.edu.cn/xjInfoAction.do?oper=xjxx"
GRADE = "http://bksjw.chd.edu.cn/bxqcjcxAction.do"

class iCHD(object):
    def __init__(self, username, user_info=None, session=None):
        self.username = username
        user_info = collections.OrderedDict()
        self.__user_info = user_info
        self.session = session

    @property
    def user_info(self):
        return self.__user_info

    @user_info.setter
    def user_info(self, value):
        self.__user_info = value

    def login(self, login_type):
        if login_type == "URP":
            with requests.Session() as self.session:
            #self.session = requests.Session()
                init_session = self.session.get(BASE_URP_URL)
                if init_session.status_code == 200:
                    print("建立连接成功！")
            data = {'zjh':self.username,'mm':self.username,'dllx':'dldl'}
            index = self.session.post(LOGIN_URL,data=data, headers=HEAD)
            if index.status_code == 200:
                print("登陆成功")

        """********************************Get user's image******************************
        image = session.get(IMG_URL)
        global img_content
        img_content = image.content
        ********************************************************************************"""
        """
            user_info_index = session.get(USER_INFO_URL,headers=HEAD)
            soup = user_info_index.text#content.decode('utf-8')
            return soup
            """

    def get_content(self):
        raw_content = collections.OrderedDict()
        grade = self.session.get(GRADE, headers=HEAD)
        user_info = self.session.get(USER_INFO_URL, headers=HEAD)
        grade_content = grade.text
        user_info_content = user_info.text
        raw_content['grade'] = grade_content
        raw_content['user_info'] = user_info_content
        return raw_content

    def parse_grade(self, raw_content):
        """*****************Get grade****************"""

        #raw_content = raw_content.decode('utf-8')
        soup = BeautifulSoup(raw_content, "lxml")
        soup = soup.find_all("tr", attrs={"class":"odd"})
        test = []
        courses = []
        for values in soup:
            values = values.find_all('td')
            #print(values)
            for value in values:
                value = value.string.strip()
                test.append(value)
            courses.append(test) # courses save all the information of all courses
            test = []
        #print(courses)
        tmp = {}
        course = {}
        for value in courses:
            course[value[2]] = value[6]
            #course.append(tmp)
            #tmp = {}
        self.user_info['course'] = course

    def parse_user_info(self, user_info_content):
        soup = BeautifulSoup(user_info_content, 'lxml')
        id_num = soup.find_all('td', attrs={'width':'275'})
        user_info_list = []
        for i in id_num:
            user_info_list.append(i.string.strip())
    #print(user_info_list)
        user_info = collections.OrderedDict()
        try:
            #user_info['school_id'] = user_info_list[0]
            #user_info['name'] = user_info_list[1]
            """
            user_info['id'] = user_info_list[5]
            user_info['sex'] = user_info_list[6]
            user_info['attr'] = user_info_list[7]
            user_info['group'] = user_info_list[11]
            user_info['grade'] = user_info_list[17]
            user_info['colleage'] = user_info_list[25]
            user_info['major'] = user_info_list[26]
            user_info['class'] = user_info_list[29]
            user_info['province'] = user_info_list[15]
            """
            self.user_info['name'] = user_info_list[1]
        except IndexError as err:
            print("用户不存在!")
            return 0

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
    print("***********************************************************")
    print("欢迎使用，本程序最新版本请在http://pan.baidu.com/s/1mhDXwEG下载")
    print("本次更新: 0. 增加选项功能 1.添加查看所借书籍功能")
    print("PS: 目前这两个功能都是不需要输入密码的(图书馆的除非自己修改了密码)，下个版本会增加显示校园卡余额，课程表等功能。会需要输入信息门户密码。不过请放心， 程序不会泄露出去也不会有后门。相关源码都可以在我的Github上查看。有bug请反馈给我(603750199@qq.com)，谢谢。")
    print("************************************************************")
    while True:
        while True:
            option = input("请选择功能(输入对应信号): 1.查询本学期成绩 2.查看所借的书籍及续借 3.教务系统 4. 退出程序: ")
            if int(option) == None or int(option) not in [1, 2, 3, 4]:
                print("输入有误，请重新输入")
                continue
            break
        if int(option) == 1:
            print("说明: 如果输入学号后长时间未响应请重启程序".center(200,"*"))
            username = get_input("请输入你的学号: ","username")
            username = str(username)
            user = iCHD(username)
            user.login(username)
            user.login("URP")
            raw_content = user.get_content()
            user.parse_user_info(raw_content['user_info'])
            user.parse_grade(raw_content['grade'])
            welcome = "欢迎你, {0}".format(user.user_info['name'])
            print(welcome.center(200,"*"))
            print("你本学期的成绩为: ".center(200,"*"))
            for key, value in user.user_info['course'].items():
                print("{0} : {1}".format(key, value if len(str(value)) != 0 else "还未公布"))
            continue

        elif int(option) == 2:
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
            continue

        elif int(option) == 3:
            Portal.main()

        elif int(option) == 4:
            confirm = input("确认要退出吗? (y/n): ")
            if confirm == 'y' or confirm == 'Y':
                print("谢谢使用")
                sys.exit()
            else:
                continue
    os.system("pause")


if __name__ == "__main__":
    main()
