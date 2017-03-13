#-*- coding:utf-8 -*-
#__author__: Leo Luo
import os
import string
import collections

def main():
    init()
    filename = input_Filename('Choose filename: ')
    content = get_Content(filename)
    if read_Data(filename) == 0:
        print("-- no items are in the list --")
        opt = input("[A]dd [Q]uit: ")
    else:
        print(read_Data(filename))
        while True:
            opt = input("[A]dd [D]elete [S]ave [Quit] [a]: ")
            if opt == 'a' or opt == 'A':
                item = input("Add item: ")
                content.append(item)
                print(content)
                tmp = ""
                to_save_item = ""
                to_save = []
                for lino,line in enumerate(content,start=1):
                    tmp = str(lino) + ": " + str(line)
                    to_save_item = tmp + "\n"
                    to_save.append(to_save_item)
                    print(tmp)
            elif opt == 's' or opt == 'S':
                print(to_save)
                write_Data(filename,to_save)
            elif opt == 'd' or opt == 'D':
                index = input("Delete item number (or 0 to cancel): ")
                delete_Data(to_save,index)
            elif opt == 'q' or opt == 'Q':
                quit_Program()
                if len(content) != len(to_save):
                    opt = input("Save unsaved changes? (y/n)")
                    if opt == 'y' or opt == 'Y':
                        pass
                    else:
                        quit_Program()
            else:
                print("EOOOR: invalid choice--enter one of 'AaDdSsQq'\nPress Enter to continue")
                continue

def quit_Program():
    print("Thanks for using it.Have a nice day!")
    os._exit(0)

def init():
    if len(get_filename()) == 0:
        cre_filename = input("--no file in this directory.please input the new file's name--\n")
        create_file(cre_filename)
    else:
        while True:
            try:
                m_quan = input("Total {0} {1}, enter the quantity of files you want show,or enter 0 to create a new file:  ".format(len(get_filename()),'file' if len(get_filename()) == 1 else 'files'))
            except ValueError as err:
                print("Wrong input!",err)
            try:
                if len(get_filename()) < int(m_quan):
                    print("Wrong input!")
                    continue
                if int(m_quan) == 0:
                    cre_filename = input("please input the new file's name--\n")
                    create_file(cre_filename)
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
def user_options(option):
    while True:
        print("[A]dd [D]elete [S]ave [Quit] [a]: ")
        if option == 'A' or option == 'a':
            item = input("Add item: ")
            break
        elif option == 'D' or option == 'd':
            pass
            break
        elif option == 'S' or option == 's':
            pass
            break
        else:
            print("Wrong input!")
            continue

def read_Data(filename):
    file_object = open(filename,encoding='utf-8')
    try:
        all_item = file_object.read()
        if len(all_item) == 0:
            return 0
        else:
            return all_item
    except SyntaxError as err:
        print(err)
    finally:
        file_object.close()

def write_Data(filename,to_save):
    file_object = open(filename,'w')
    try:
        for value in to_save:
            file_object.write(value)
        print("Saved")
    finally:
        file_object.close()
"""
******Get file's content to a list*********
"""
def get_Content(filename):
    file_object = open(filename,encoding='utf-8')
    file_content = []
    content = {}
    try:
        for line in file_object:
            chars = ':'
            line = line.strip().split(chars)
            file_content.append(line)
        for lists in file_content:
            content.setdefault(lists[0],lists[1])
        #print(content)
        return content
    finally:
        file_object.close()

def delete_Data(to_save,index):
    del_map = {}

    contents_map.pop(index)


def create_file(filename):
    if not filename.endswith('.lst'):
        filename += '.lst'
    try:
        created_file = open(filename,'w')
        print("{0} has been created!\n".format(filename))
    finally:
        created_file.close()

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

def input_Filename(msg="Input the file's name"):
    user_input = input(msg)
    if not user_input.endswith('.lst'):
        user_input += '.lst'
    return user_input

if __name__ == '__main__':
    main()
