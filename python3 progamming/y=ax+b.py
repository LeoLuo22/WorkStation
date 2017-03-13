#-*- coding:utf-8 -*-
#__author__: Leo Luo

import math

def get_Values(msg):
    values = []
    stop_flag = " "
    try:
        while True:
            value = input(msg)
            if str(value) == " ":
                break
            values.append(float(value))
    except ValueError as err:
        print(err)
    return values

def main():
    X = get_Values("Enter x: ")
    Y = get_Values("Enter y:")
    N = len(X)
    sum_X = 0.0
    sum_X_2 = 0.0
    for x in X:
        sum_X += x
        sum_X_2 += x * x
    sum_Y = 0.0
    sum_XY = 0.0
    for y in Y:
        sum_Y += y
    for x,y in X,Y:
        sum_XY += x * y
    a = (N * sum_XY - sum_X * sum_Y) / (N * sum_X_2 - (sum_X) ** 2)
    b = 1 / N * sum_Y - a * (1 / N) * sum_X
    print("y = {0}x + {1}".format(a,b))



if __name__ == '__main__':
    main()


