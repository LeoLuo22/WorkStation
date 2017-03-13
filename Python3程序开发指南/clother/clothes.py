#-*- coding:utf-8 -*-
#__author__: Leo Luo
import os

def main():
    init()

def cal_aver(content):
    m_aver = []
    m_sum = 0.0
    aver = 0.0
    for items in content:
        for i in range(1,(len(items)-1)):
            m_sum += float(items[i])
        aver = m_sum / (len(items) - 2)
        m_aver.append(aver)
        m_sum = 0.0
        aver = 0.0
    for i in range(0,len(content)):
        content[i].append(m_aver[i])
    return content

def quit_Program():
    print("Thanks for using it.Have a nice day!")
    os._exit(0)

def init():
    if len(get_filename()) == 0:
        filename = input("--no file in this directory.please input the new file's name--\n")
        content = cal_aver(new_data())
        write_Data(filename,content)
    else:
        while True:
            try:
                m_quan = input("Total {0} {1}, enter 0 to create a new file:  ".format(len(get_filename()),'file' if len(get_filename()) == 1 else 'files'))
            except ValueError as err:
                print("Wrong input!",err)
            if len(get_filename()) < int(m_quan):
                print("Wrong input!")
                continue
            elif int(m_quan) == 0:
                cre_new_file_content()
                continue
            else:
                filename = input_Filename("Choose filename:")
                read_Data(get_Content(filename))
                break

def cre_new_file_content():
    filename = input_Filename()
    content = cal_aver(new_data())
    write_Data(filename,content)

def read_Data(content):
    m_show = ""
    for values in content:
        for v in values:
            m_show += v
            m_show += " "
        print(m_show)
        m_show = ""

def write_Data(filename,content):
    if not filename.endswith(".txt"):
        filename += ".txt"
    file_object = open(filename,'w',encoding='utf-8')
    try:
        for values in content:
            for v in values:
                v = str(v)
                v += " "
                file_object.write(v)
            file_object.write("\n")
    finally:
        file_object.close()

def get_Content(filename):
    file_object = open(filename,encoding='utf-8')
    file_content = []
    content = []
    try:
        for line in file_object:
            line = line.split()
            content.append(line)
        return content
    except FileNotFoundError as err:
        print(err)
    finally:
        file_object.close()

def show_Current(cur_list):
    cur_list.sort(key=str.lower)
    for lino,line in enumerate(cur_list,start=1):
        print("{0}: {1}".format(lino,line))

def delete_Data(to_save,index):
    tmp = to_save[index-1]
    to_save.pop(index-1)
    print("'{0}' has been deleted".format(tmp))

def get_filename():
    file_list = []
    try:
        m_rst = os.listdir(".")
    except NotImplementedError as err:
        print(err)
    for rst in m_rst:
        if  rst.endswith('.txt'):
            file_list.append(rst)
    return file_list

def input_Filename(msg="Input the file's name: "):
    user_input = input(msg)
    if not user_input.endswith('.txt'):
        user_input += '.txt'
    return user_input

def new_data():
    s = "平均值: "
    m_content = []
    content = []
    while True:
        v = input("请输入项目名称:")
        if str(v) == "end":
            break
        m_content.append(v)
        while True:
            value = input("请输入{0}的值: ".format(v))
            if str(value) == "end":
                break
            m_content.append(value)
        m_content.append(s)
        content.append(m_content)
        m_content = []
    return content

def add_Data(content):
    m_content = []
    for items in content:
        m_data = input("请输入{0}的值: ".format(items[0]))
        items.append(m_data)
        m_content.append(items)
    return m_content

if __name__ == '__main__':
    main()
