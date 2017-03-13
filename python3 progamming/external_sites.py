#-*- coding:utf-8 -*-
#__author__: Leo Luo

import sys
import collections

sites = collections.defaultdict(set)

if len(sys.argv) == 1 or sys.argv[1] in ('-h','--help'):
    print("usage: {0} file".format(sys.argv[0]))
else:
    for filename in sys.argv[1:]:
        for line in open(filename):
            i = 0
            while True:
                site = None
                i = line.find("http://",i)#没有找到返回-1,找到返回最左位置
                if i > -1:
                    i += len("http://")#i = 7
                    for j in range(i,len(line)):
                        if not (line[j].isalnum() or line[j] in ".-"):
                            site = line[i:j].lower()
                            break
                if site and "." in site:
                    sites.setdefault(site,set()).add(filename)
                    i = j
                else:
                    break

for site in sorted(sites):
    print("{0}".format(site))
    """
    for filename in sorted(sites[site],key=str.lower):
        print("    {0}".format(filename))
        """
