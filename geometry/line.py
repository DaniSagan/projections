from __future__ import print_function

__author__ = 'daniel'

from vec3 import Vec3
from enum import Enum
import math


class Direction(Enum):
    POSITIVE = 0
    NEGATIVE = 1


class Line(object):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def get_point(self, param):
        return self.origin + (param*self.direction)

    def get_closest_point_to(self, point):
        l = self.direction.get_unit()
        return self.origin + (Vec3.dot(Vec3.from_to(self.origin, point), l)*l)

    def get_dist_to_point(self, point):
        return abs(Vec3.from_to(point, self.get_closest_point_to(point)))

    def get_point_at_dist(self, point, dist, direction=Direction.POSITIVE):
        closest = self.get_closest_point_to(point)
        dist_to_point = self.get_dist_to_point(point)
        if dist_to_point > dist:
            raise ValueError('Parameter dist must be greater than the shortest distance from the point to the line. dist_to_point: {0}, dist: {1}'.format(dist_to_point, dist))
        if direction == Direction.POSITIVE:
            return closest + math.sqrt(dist**2 - dist_to_point**2)*self.direction.get_unit()
        else:
            return closest - math.sqrt(dist**2 - dist_to_point**2)*self.direction.get_unit()

    def __repr__(self):
        return '<Line, origin: {origin}, direction: {direction}>'.format(origin=self.origin, direction=self.direction)
