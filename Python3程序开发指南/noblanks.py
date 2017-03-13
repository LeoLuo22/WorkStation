#-*- coding: utf-8 -*-
#__author__: Leo Luo

import string

filename = input("Enter the path of file:\n")

def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename, encoding='utf-8')
        for line in fh:
            lines.append(line.strip().replace(' ',''))
    except (IOError,OSError) as err:
        print(err)
        return []
    except EnvironmentError as err:
        print(err)
        return[]
    finally:
        if fh is not None:
            fh.close()
    return lines

if __name__ == '__main__':
    print(read_data(filename))
