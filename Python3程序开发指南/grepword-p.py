# -*- coding:utf-8 -*-
__author__ = "Leo Luo"

import os
import sys
import subprocess

def main():
    child = os.path.join(os.path.dirname(__file__), "grepowrd-p-child.py") #获取子程序名称
    opts, word, args = parse_options()
    filelist = get_file(args, opts.recurse)
    files_per_process = len(filelist) #opts.count
    start, end = 0, files_per_process + (len(filelist) % opts.count)
    number = 1
    pipes = []
    while start < len(filelist):
        command  = [sys.executable, child]
        if opts.debug:
            command.append(str(num))
        pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
        pipes.append(pipe)
        pipe.stdin.write(word.encode("utf-8") + b"\n")
        for filename in filelist[start:end]:
            pipe.stdin.write(filename.encode("utf-8") + b"\n")
        pipe.stdin.close()
        number += 1
        start, end = end, end + files_per_process
