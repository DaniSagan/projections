from __future__ import print_function

__author__ = 'daniel'

import line
from line import Line
from vec2 import Vec2
from vec3 import Vec3
from plane import Plane
import inspect


class View(object):
    """ Class that represents a perspective projection in 3D."""

    def __init__(self, screen_dist):
        self.screen_dist = screen_dist
        self.transforms = []

    def line(self, screen_point):
        """ Returns the line object defined by the camera position and the screen position. """
        return Line(Vec3(0, 0, 0), Vec3(screen_point.x, screen_point.y, -self.screen_dist))

    def apply_transforms(self, point):
        """ Apply the current transforms to the point passed as parameter. """
        tr_point = point
        for tr in self.transforms:
            tr_point = tr.transform(tr_point)
        return tr_point

    def project_point(self, point):
        tr_point = self.apply_transforms(point)
        if tr_point.z > -self.screen_dist:
            raise ValueError('Error: transformed point lies behind the screen. Point: ' + str(point) + ' Transformed: ' + str(tr_point) + 'Transforms: ' + str(self.transforms))
        else:
            return Vec2(-self.screen_dist*tr_point.x/tr_point.z, -self.screen_dist*tr_point.y/tr_point.z)

    def project_points(self, points):
        return map(lambda p: self.project_point(p), points)

    def project_line(self, line):
        return self.project_points(line.get_vertices())

    def push_transform(self, transform):
        self.transforms.append(transform)

    def push_transforms(self, *transforms):
        for t in transforms:
            self.transforms.append(t)

    def pop_transform(self):
        return self.transforms.pop()

    def clear_transforms(self):
        self.transforms = []

    def get_plane(self, sp1, sp2, sp3, dist_21, dist_23, ang_13):
        """ Returns the plane object defined by three points projected onto some unknown perspective.
        :param sp1: screen point 1
        :param sp2: screen point 2
        :param sp3: screen point 3
        :param dist_21: real distance from 2 to 1
        :param dist_23: real distance from 2 to 3
        :param ang_13: angle between vectors sp1-sp2 and sp2-sp3
        :return: plane in real coordinates
        """
        l01 = self.line(sp1)
        l02 = self.line(sp2)
        l03 = self.line(sp3)
        param = 0
        a = l02.get_point(param)
        t1 = l01.get_point_at_dist(a, dist_21, line.Direction.POSITIVE)
        t3 = l03.get_point_at_dist(a, dist_23, line.Direction.POSITIVE)
        ang = Vec3.angle_between(t1-a, t3-a)
        while abs(ang-ang_13) > 0.001:
            param += 10.0*abs(ang-ang_13)
            while True:
                a = l02.get_point(param)
                try:
                    t1 = l01.get_point_at_dist(a, dist_21, line.Direction.POSITIVE)
                    t3 = l03.get_point_at_dist(a, dist_23, line.Direction.POSITIVE)
                    break
                except ValueError:
                    param -= 0.1*abs(ang-ang_13)
            ang = Vec3.angle_between(t1-a, t3-a)
            i = inspect.getframeinfo(inspect.currentframe())
        return Plane(a, t1-a, t3-a)
