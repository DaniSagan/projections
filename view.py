from line import Line
from vec2 import Vec2

class View(object):
    def __init__(self, screen_dist):
        self.screen_dist = screen_dist

    def line(self, screen_point):
        return Line(Vec3(0,0,0), Vec3(screen_point.x, screen_point.y, -self.screen_dist))
        
    def project(self, point):
        if point.z > -self.screen_dist:
            raise ValueError('point.z must be less than view.dist')
        else:
            return Vec2(-self.screen_dist*point.x/point.z, -self.screen_dist*point.y/point.z)
