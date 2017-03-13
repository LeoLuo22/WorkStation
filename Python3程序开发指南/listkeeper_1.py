#-*- coding:utf-8 -*-
#__author__: Leo Luo
import os
import string

OPTIONS = ('a','A','s','S','d','D','q','Q',0)

def main():
    init()
    filename = input_Filename('Choose filename: ')
    content = get_Content(filename)
    ori_content = get_Content(filename)
    if read_Data(filename) == 0:
        print("-- no items are in the list --")
        opt = input("[A]dd [Q]uit: ")
        if opt == 'a' or opt == 'A':
            item = input("Add item: ")
            content.append(item)
        while True:
            print(content)
            opt = input("[A]dd [D]elete [S]ave [Quit] [a]: ")
            if opt == 'a' or opt == 'A':
                item = input("Add item: ")
                content.append(item)
            elif opt == 's' or opt == 'S':
                write_Data(filename,content)
                changes = abs(len(content)-len(ori_content))
                print("Saved {0} {1} to {2}".format(changes,'item' if changes <=1 else 'items',filename))
            elif opt == 'd' or opt == 'D':
                index = input("Delete item number (or 0 to cancel): ")
                opt = input("Are you sure to delete?<y/n>")
                if opt == 'y':
                    delete_Data(content,int(index))
                    show_Current(content)
                else:
                    continue
            elif opt == 'q' or opt == 'Q':
                if content != ori_content:
                    opt = input("Save unsaved changes? (y/n)")
                    if opt == 'y' or opt == 'Y':
                        write_Data(filename,content)
                        quit_Program()
                    else:
                        quit_Program()
            else:
                print("ERROR: invalid choice--enter one of 'AaDdSsQq'")
                y = input("Press Enter to continue")
                if y == 'y':
                    continue

    else:
        print(read_Data(filename))
        while True:
            opt = input("[A]dd [D]elete [S]ave [Quit] [a]: ")
            if opt == 'a' or opt == 'A':
                item = input("Add item: ")
                content.append(item)
                show_Current(content)
            elif opt == 's' or opt == 'S':
                write_Data(filename,content)
                changes = abs(len(content)-len(ori_content))
                print("Saved {0} {1} to {2}".format(changes,'item' if changes <=1 else 'items',filename))
            elif opt == 'd' or opt == 'D':
                index = input("Delete item number (or 0 to cancel): ")
                opt = input("Are you sure to delete?<y/n>")
                if opt == 'y':
                    delete_Data(content,int(index))
                    show_Current(content)
                else:
                    continue
            elif opt == 'q' or opt == 'Q':
                if content != ori_content:
                    opt = input("Save unsaved changes? (y/n)")
                    if opt == 'y' or opt == 'Y':
                        write_Data(filename,content)
                        quit_Program()
                    else:
                        quit_Program()
            else:
                print("ERROR: invalid choice--enter one of 'AaDdSsQq'")
                y = input("Press Enter to continue...")
                if y == None:
                    continue
                continue

class InputError(Exception):
    print("Wrong Input! ")

def get_Option(msg):
    opt = input(msg)
    flag = 0
    for i in OPTIONS:
        if opt == i:
            flag += 1
    if flag == 0:
        raise InputError()
    else:
        return opt

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

def write_Data(filename,content):
    content.sort(key=str.lower)# = sorted(contents,key=str.lower)
    file_object = open(filename,'w',encoding='utf-8')
    tmp = ""
    to_save_item = ""
    to_save = []
    for lino,line in enumerate(content,start=1):
        tmp = str(lino) + ": " + str(line)
        to_save_item = tmp + "\n"
        to_save.append(to_save_item)
    try:
        for value in to_save:
            file_object.write(value)
    finally:
        file_object.close()

def get_Content(filename):
    file_object = open(filename,encoding='utf-8')
    file_content = []
    content = []
    try:
        for line in file_object:
            chars = ':'
            line = line.strip().split(chars)
            file_content.append(line)
        for lists in file_content:
            content.append(lists[1][1:])
        return content
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
