# -*- coding: utf-8 -*-
# author: yse
# time: 2020-07-02

import math
from collections import Sequence


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __mul__(self, other):
        return Vector(self.x*other, self.y*other)

    def __abs__(self):
        return math.hypot(self.x, self.y)


print Vector(1, 2) + Vector(2, 3)
print Vector(1, 2) * 10
print bool(Vector(1, 2))
