from __future__ import print_function
import line
from line import Line
from vec2 import Vec2
from vec3 import Vec3
import utils
from plane import Plane

class View(object):
    def __init__(self, screen_dist):
        self.screen_dist = screen_dist
        self.transforms = []

    def line(self, screen_point):
        return Line(Vec3(0,0,0), Vec3(screen_point.x, screen_point.y, -self.screen_dist))

    """def project(self, point):
        if point.z > -self.screen_dist:
            raise ValueError('point.z must be less than view.dist')
        else:
            return Vec2(-self.screen_dist*point.x/point.z, -self.screen_dist*point.y/point.z)"""

    def apply_transforms(self, point):
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

    def pop_transform(self):
        return self.transforms.pop()

    def get_plane(self, sp1, sp2, sp3, dist_21, dist_23, ang_13):
        l01 = self.line(sp1)
        l02 = self.line(sp2)
        l03 = self.line(sp3)
        param = 0
        a = l02.get_point(param)
        t1 = l01.get_point_at_dist(a, dist_21, line.Direction.POSITIVE)
        t3 = l03.get_point_at_dist(a, dist_23, line.Direction.POSITIVE)
        ang = Vec3.angle_between(t1-a, t3-a)
        while abs(ang-ang_13) > 0.00001:
            param += 0.01*abs(ang-ang_13)
            a = l02.get_point(param)
            t1 = l01.get_point_at_dist(a, dist_21, line.Direction.POSITIVE)
            t3 = l03.get_point_at_dist(a, dist_23, line.Direction.POSITIVE)
            ang = Vec3.angle_between(t1-a, t3-a)
        return Plane(a, t1-a, t3-a)
