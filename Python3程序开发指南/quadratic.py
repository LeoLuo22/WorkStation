#-*- coding:utf-8 -*-
#__author__: Leo Luo
import cmath
import math
import sys

print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")

def get_float(msg,allow_zero):
    x = None
    while x is None:
        try:
            x =float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
    return x

a = get_float("enter a: ",False)
b = get_float('enter b: ',True)
c = get_float("enter c: ",True)

x1 = None
x2 = None

discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x1 = -(b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else:
        root = cmath.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)

if __name__ == '__main__':
    equation = "{0}x\N{SUPERSCRIPT TWO}".format(a)
    if b != 0:
        if b < 0:
            equation += " - {0}x".format(abs(b))
        else:
            equation += " + {0}x".format(b)
    if c != 0:
        if c < 0:
            equation  += " - {0} ".format(abs(c),x1)
        else:
            equation += " + {0} ".format(c,x1)
    equation += " = 0 x\N{RIGHTWARDS ARROW} = {0}".format(x1)
    if x2 is not None:
        equation += " or x = {0}".format(x2)
    print(equation)
