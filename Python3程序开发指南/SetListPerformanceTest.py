# -*- coding:utf-8 -*-

import random
import time

NUMBER_OF_ELEMENTS = 10000

lst = list(range(NUMBER_OF_ELEMENTS))
random.shuffle(lst)

s = set(lst)

startTime = time.time()
for i in range(NUMBER_OF_ELEMENTS):
    i in s
endTime = time.time()
runTime = int((endTime - startTime) * 1000)
print("To test if {0} elements are in the set\n. The run time is {1} millionseconds".format(NUMBER_OF_ELEMENTS, runTime))

startTime = time.time()
for i in range(NUMBER_OF_ELEMENTS):
    i in lst
    #print(i)
endTime = time.time()
runTime = int((endTime - startTime) * 1000)
print("To test if {0} elements are in the list\n. The run time is {1} millionseconds".format(NUMBER_OF_ELEMENTS, runTime))
