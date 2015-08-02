import math
import numpy as np
import utils

class Vec3(object):
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return "<{x}, {y}, {z}>".format(x=self.x, y=self.y, z=self.z)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __sub__(self, other):
        return Vec3(self.x-other.x, self.y-other.y, self.z-other.z)

    def __add__(self, other):
        return Vec3(self.x+other.x, self.y+other.y, self.z+other.z)

    def __mul__(self, value):
        return Vec3(self.x*value, self.y*value, self.z*value)

    def __rmul__(self, value):
        return self.__mul__(value)

    def get_unit(self):
        return self*(1./abs(self))

    def as_matrix(self):
        return np.matrix([self.x, self.y, self.z]).T

    @staticmethod
    def from_matrix(m):
        return Vec3(m.item(0), m.item(1), m.item(2))

    def rotate(self, axis, angle):
        return Vec3.from_matrix(utils.rotation_matrix(axis, angle)*self.as_matrix())

    def translate(self, movement):
        return self+movement

    @staticmethod
    def cross(v1, v2):
        return Vec3(v1.y*v2.z-v1.z*v2.y,
                    v1.z*v2.x-v1.x*v2.z,
                    v1.x*v2.y-v1.y*v2.x)

    @staticmethod
    def dot(v1, v2):
        return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z

    @staticmethod
    def from_to(v1, v2):
        return v2-v1
