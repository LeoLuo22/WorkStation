#-*- coding:utf-8 -*-
#__author__: Leo Luo
import os
import string
"""
*************TO-DO LIST*****************
0.读取文件，修改文件
1.保存文件&文件名
2.删除文件
3.提示用户选项
********************************************
"""
def main():
    """
    如果为空则创建文件名
    """
    if len(get_filename()) == 0:
        cre_file = input("--no file in this directory.please input the new file's name--\n")
        if not cre_file.endswith('.lst'):
            cre_file += '.lst'
            print(cre_file)
        created_file = open(cre_file,'w')
    else:
        while True:
            try:
                m_quan = input("Total {0} {1}, enter the quantity of files you want show: ".format(len(get_filename()),'file' if len(get_filename()) == 1 else 'files'))
            except ValueError as err:
                print("Wrong input!",err)
            try:
                if len(get_filename()) < int(m_quan):
                    print("Wrong input!")
                    continue
            except ValueError as err:
                print("Wrong input!")
            else:
                clipped_file = []
                for i in range(0,int(m_quan)):
                    clipped_file.append(get_filename()[i])
                for  lino,line in enumerate(clipped_file,start=1):
                    print("{0}  {1}".format(lino,line))
                break
    read_data('C:\Users\Leo\Desktop\python3\test0.lst')
def user_options(option):
    print("[A]dd [D]elete [S]ave [Quit] [a]: ")

def read_data(file):
    item = open(filename).decode('unicode').encoding('utf-8')
    print(item.read())
    item.close()

def create_file(filename):
    pass
def get_filename():
    file_list = []
    try:
        m_rst = os.listdir(".")
    except NotImplementedError as err:
        print(err)
    for rst in m_rst:
        if  rst.endswith('.lst'):
            file_list.append(rst)
    return file_list

#print(get_filename())

if __name__ == '__main__':
    main()
