#-*-coding:utf-8-*-
#__author__:Leo Luo
import sys
import unicodedata

def print_unicode_table(word):
    print("decimal    hex    chr    {0:^40}".format("name"))#字符串规约：中间对齐，在40字符宽中间位置打印name
    print("-------    ------ ---   {0:-<40}".format(""))#用-填充，左对齐

    code = ord(" ")
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c,"*** unknown ***")
        if word is None or word in name.lower():
            print("{0:7}    {0:5x}    {0:^3c}    {1}".format(code,name.title()))#s.title():Return the copy of s,every word's first character of s is to upper
        code += 1

word = None
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h","--help"):
        print("usage: {0} [string]".format(sys.argv[0]))
        word = 0
else:
    word = sys.argv[1].lower()
if word != 0:
    print_unicode_table(word)

