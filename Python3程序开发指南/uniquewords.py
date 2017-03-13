#-*- coding:utf-8 -*-
#__author__: Leo Luo

import string
import sys

words = {}
chars = string.whitespace + string.punctuation + string.digits + "\""
if len(sys.argv) == 1 or sys.argv[1] in ('-h','--help'):
    print("Usage {0} file1 file2...".format(sys.argv[0]))
else:
    for filename in sys.argv[1:]:
        for line in open(filename):
            for word in line.lower().split():
                word = word.strip(chars)
                if len(word) >= 2:
                    words[word] = words.get(word,0) + 1

words = sorted(words.items(),key = lambda d:d[1],reverse = True)
for word in words:
    print("'{0}' occurs {1} {2}".format(word[0],word[1],('times' if word[1] > 1 else 'time')))
"""
words = sorted(words.items(),key = lambda w:w[1],reverse = True)
for word in words:
    print("'{0}' occurs {1} times".format(word,words[word]))
"""
