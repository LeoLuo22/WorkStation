"""这个小程序是用来记录我的体重的"""
import sqlite3
from utils.mysqlite import MySqlite
from datetime import datetime

class User():
    def __init__(self, username=None, passwd=None):
        """建立用户
            @param username
             用户名
            @param passwd
             密码
        """
        self.sqlite = MySqlite('data.db', 'user')
        self.username = username
        self.passwd = passwd

    def login(self):
        """用户登陆"""
        username = self.sqlite.find_one(username=self.username)
        if not username:
            print('The user is not exist')
            answer = input('Do you want to register this user?(y/n)')
            if answer == 'y':
                return self.signup(self.username)
            else:
                return
        try:
            password = self.sqlite.find_one(username=self.username).get('password')
        except sqlite3.OperationalError:
            self.sqlite.newtable('user', username='varchar(20) primary key', password='varchar(20)')
            return self.login()

        if self.passwd == password:
            print('Login success')
            return True
        else:
            print('Wrong password, try again: ')
            new_password = input()
            self.passwd = new_password
            return self.login()

    def signup(self, username=None):
        if not username:
            username = input('Enter a new username: ')
        old = self.sqlite.find_one(username=username)
        if old:
            return self.signup()
        password = input('Enter your password: ')
        self.sqlite.create('user', username=username, password=password)

class Information():
    def __init__(self, username):
        """初始化连接， 只有认证过的用户才能使用
            @param username
             用户名
        """
        self.username = username
        self.sqlite = MySqlite('data.db', username)

    def newtable(self):
        sqlite = MySqlite('data.db')
        sqlite.newtable(self.username, date='varchar(20) primary key', height='varchar(20)',
                        weight='varchar(20)', bmi='varchar(20)')
        self.sqlite = MySqlite('data.db', self.username)

    def insert(self, weight, height):
        date = str(datetime.now())[:-7]
        bmi = str(self.bmi(weight, height))
        try:
            self.sqlite.create(self.username, date=date, height=str(height),
                               weight=str(weight), bmi=str(bmi))
        except sqlite3.OperationalError:
            self.newtable()
            self.insert(weight, height)

    def bmi(self, weight, height):
        """计算体质指数
        @param weight
         体重
        @return
         bmi
    """
        if not isinstance(weight, float):
            raise ValueError("Wrong Arguments")
        if not isinstance(height, float):
            raise ValueError("Height shoule be float")

        return round(weight / height ** 2, 2)

def main():
    #weight = float(input("今天你的体重："))
    #print(get_bmi(73.0, 1.68))
    username = input('Enter username: ')
    password = input('Enter password: ')
    user = User(username, password)
    if user.login():
        info = Information(username)
        weight = float(input('Enter your weight today: (kg)'))
        height = float(input('Enter your height today: (m)'))
        info.insert(weight, height)
        print('Your bmi is ', info.bmi(weight, height))


if __name__ == '__main__':
    main()
