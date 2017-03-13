#-*- coding:utf-8 -*-
#__author__: Leo Luo

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        return Point(self,x - other.x, self.y - other.y)

    def __mul__(self,other):
        return Point(self.x * other, self.y * other)

    def __imul__(self,other):
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def __itruediv__(self, other):
        return Point(self.x / other, self.y / other)

    def __floordiv__(self, other):
        return Point(self.x // other, self.y // other)

    def __ifloordiv__(self, other):
        return Point(self.x // other, self.y // other)

