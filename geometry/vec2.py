__author__ = 'daniel'

import math
import numpy as np


class Vec2(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "<{x}, {y}>".format(x=self.x, y=self.y)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __sub__(self, other):
        return Vec2(self.x-other.x, self.y-other.y)

    def __add__(self, other):
        return Vec3(self.x+other.x, self.y+other.y)

    def __mul__(self, value):
        return Vec2(self.x*value, self.y*value)

    def __rmul__(self, value):
        return self.__mul__(value)

    def __neg__(self):
        return -1.*self

    def get_unit(self):
        return self*(1./abs(self))

    def as_matrix(self):
        return np.matrix([self.x, self.y]).T

    def apply(self, fn):
        return Vec2(fn(self.x), fn(self.y))

    def reduce(self, fn, init_value=0.):
        return reduce(fn, self.tuple(), init_value)

    def tuple(self):
        return self.x, self.y

    @staticmethod
    def dot(v1, v2):
        return v1.x*v2.x + v1.y*v2.y

    @staticmethod
    def from_to(v1, v2):
        return v2-v1

    @staticmethod
    def get_xy_lists(lst):
        return [v.x for v in lst], [v.y for v in lst]
