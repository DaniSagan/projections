from vec3 import Vec3

class BoundingBox(object):
    def __init__(self, point=None):
        self.vmin = point
        self.vmax = point

    def get_center(self):
        return 0.5*(self.vmin + self.vmax)

    def bound_point(self, point):
        if (self.vmin is None) or (self.vmax is None):
            self.vmin = point
            self.vmax = point
        else:
            if point.x < self.min.x:
                self.min.x = point.x
            if point.y < self.min.y:
                self.min.y = point.y
            if point.z < self.min.z:
                self.min.z = point.z
            if point.x > self.max.x:
                self.max.x = point.x
            if point.y > self.max.y:
                self.max.y = point.y
            if point.z > self.max.z:
                self.max.z = point.z
