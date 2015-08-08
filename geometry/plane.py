__author__ = 'daniel'

from vec3 import Vec3


class Plane(object):
    def __init__(self, origin, direction1, direction2):
        self.origin = origin
        self.direction1 = direction1
        self.direction2 = direction2

    def get_point(self, param1, param2):
        return self.origin + (param1*self.direction1) + (param2*self.direction2)

    def get_normal(self):
        return Vec3.cross(self.direction1, self.direction2).get_unit()

    def get_closest_point_to(self, point):
        n = self.get_normal()
        return point - (Vec3.dot(Vec3.from_to(self.origin, point), n)*n)

    def get_dist_to_point(self, point):
        return abs(Vec3.from_to(point, self.get_closest_point_to(point)))
