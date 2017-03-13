#-*- coding:utf-8 -*-
__author__ = "Leo Luo"

import sqlite3
from datetime import datetime
import os
import sys
import collections
import shutil

class InputError(Exception):pass

class Goal(object):
    def __init__(self, ID=None, Name=None, Date=None, Success=None, Failure=None, Total=None, Rate=None, Reward=None):
        super().__init__
        self.ID = ID
        self.Name = Name
        self.Date = Date
        self.Success = Success
        self.Failure = Failure
        self.Total = Total
        self.Rate = Rate
        self.Reward = Reward

    def set_new_goal(self, db_name, Goal_name):
        if not db_name.endswith(".db"):
            db_name += ".db"
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        try:
            cur.execute("create table goal(ID interger primary key, {0} varchar(10), Date varchar(10), Success interger, Failure interger, Total interger)".format(Goal_name))
        except sqlite3.OperationalError as err:
            print("goal表已存在")
        t = (1, Goal_name, get_date(), 0, 0, 0)
        cur.execute("insert into goal values (?, ?, ?, ?, ?, ?)",t)
        conn.commit()
        conn.close()

    def __last_data(self, db_name):
        today_date = get_date()
    def write_to_db(self, date):pass

    def file_add(self, name):
        if not name.endswith(".db"):
            name += ".db"
        conn = sqlite3.connect(name)
        conn.commit()
        conn.close()

    def add_to_record(self, db_name,flag):
        if not db_name.endswith(".db"):
            name += ".db"
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        cur.execute("select * from goal order by id desc")
        result = cur.fetchall()
        #print(result)
        last_record = result[0]
        last_record_id = last_record[0]
        last_record_name = last_record[1]
        last_record_date  = last_record[2]
        last_record_success = last_record[3]
        last_record_fail = last_record[4]
        last_record_total = last_record[5]
        today = get_date()
        if last_record_date == today:
            print("你已经打过卡了")
            return 0
        if flag == True:
            last_record_id += 1
            last_record_date = get_date()
            last_record_success += 1
            last_record_total += 1
            data = (last_record_id, last_record_name, last_record_date, last_record_success, last_record_fail, last_record_total)
            cur.execute("insert into goal values (?, ?, ?, ?, ?, ?)",data)
            conn.commit()
            conn.close()
        elif flag == False:
            last_record_id += 1
            last_record_date = get_date()
            last_record_fail += 1
            last_record_total += 1
            data = (last_record_id, last_record_name, last_record_date, last_record_success, last_record_fail, last_record_total)
            cur.execute("insert into goal values (?, ?, ?, ?, ?, ?)",data)
            conn.commit()
            conn.close()


    def add(self, name):
        _name = name
        if not name.endswith(".db"):
            name += ".db"
        conn = sqlite3.connect(name)
        cur = conn.cursor()
        try:
            cur.execute("create table goal(ID interger primary key, Name varchar(10), Date varchar(10), Success interger, Failure interger, Total interger, Rate float, Reward float)")
        except sqlite3.OperationalError as err:
            print("goal表已存在")
        t = (1, _name, get_date(), 0, 0, 0, 0.1, 0)
        cur.execute("insert into goal values (?, ?, ?, ?, ?, ?, ?, ?)",t)
        conn.commit()
        conn.close()

    def show(self, db_name, sql, quantity):
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        #cur.execute("select * from goal order by id desc")
        try:
            cur.execute(sql)
        except sqlite3.OperationalError as err:
            print("错误")
            return 0
        result_lis = cur.fetchall()
        for i in range(0, quantity):
            print(result_lis[i])
        conn.commit()
        conn.close()

    def show_accomplish(self, db_name):
        if not db_name.endswith(".db"):
            name += ".db"
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        cur.execute("select * from goal order by id desc")
        result = cur.fetchall()
        last_record = result[0]
        last_record_id = last_record[0]
        last_record_name = last_record[1]
        last_record_date  = last_record[2]
        last_record_success = last_record[3]
        last_record_fail = last_record[4]
        last_record_total = last_record[5]
        conn.commit()
        conn.close()
        print("你设立这个目标已经 {0} 天了, 成功了 {1} 天，失败了 {2} 天".format(last_record_total, last_record_success, last_record_fail))



def get_input(msg, _type):
    if _type == "option":
        while  True:
            option = input(msg)
            try:
                option = int(option)
            except ValueError as err:
                print("输入有误！请重新选择。")
                get_input(msg, _type)
            try:
                if option not in range(1,50):
                    raise InputError()
            except InputError as err:
                print("Wrong input.")
                continue
            return option
    elif _type == "select_option":
        while True:
            select_option = input(msg)

def get_date():
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    if len(month) != 2:
        month = "0" + month
    day = str(datetime.now().day)
    if len(day) != 2:
        day = "0" + day
    date = year + month + day
    return date

def exist_db():
    db = collections.OrderedDict()
    _all = os.listdir('.')
    all_db = []
    for i in _all:
        if i.endswith('.db'):
            all_db.append(i)
    for lino, line in enumerate(all_db, start=1):
        db[lino] = line
    return db

def generate_sql(operation):
    if operation == "select":
        pass

def main():
    while True:
        db = exist_db()
        if len(db) == 0:
            print("There is no database file in this directory".center(200, "*"))
        else:
            print("现有的数据库文件有: ")
            for key, value in db.items():
                print("{0}   {1}".format(key,value))
        option = get_input("请选择功能: 1.新建 2.删除 3.修改 4.查询 5.退出: ", "option")
        goal = Goal()
        if option == 1:
            name = input("请输入新建数据库名称: ")
            if len(name) == 0:
                print("The name shouldn't be null".center(200,"*"))
                continue
            goal.file_add(name)
            if ((name+".db") in exist_db().values()):
                print(" {0} 已成功创建".format(name))
            goal_name = input("Enter the new goal's name: ")
            if len(goal_name) == 0:
                print("The name shouldn't be null".center(200,"*"))
                continue
            goal.set_new_goal(name, goal_name)

        elif option == 2:
            seq_num = get_input("Please input the sequence number of database file: ", "option")
            try:
                delete_db_name = db[int(seq_num)]
            except KeyError as err:
                print("An error occured: {0}".format(err).center(200,"*"))
                continue
            #print(os.getcwd())
            path = os.getcwd() + "\\" +delete_db_name
            os.remove(path)
            if delete_db_name not in exist_db().values():
                print("{0} has been successfully deleted. ".format(delete_db_name).center(200,"*"))
            continue
        elif option == 3:
            pass
        elif option == 4:
            select_option = input("请输入要查询的序号: ")
            db_name = db[int(select_option)]
            #print(db_name)
            #goal.show(db_name, "select * from goal order by id desc", 2)
            verify = input("Have you done your goal today? (y/n): ")
            if verify == "y" or verify == "Y":
                goal.add_to_record(db_name, True)
                goal.show_accomplish(db_name)
                continue
            else:
                goal.add_to_record(db_name, False)
                goal.show_accomplish(db_name)
                continue
        elif option == 5:
            print("\n" + "Thanks for using! ".center(250))
            sys.exit()

if __name__ == "__main__":
    main()



