__author__ = 'daniel'

import copy

class BoundingBox(object):
    """Class that represents a bounding box for a series of defined points.
    """
    def __init__(self, point=None):
        self.vmin = copy.deepcopy(point)
        self.vmax = copy.deepcopy(point)

    def get_center(self):
        return 0.5*(self.vmin + self.vmax)

    def bound_point(self, point):
        if (self.vmin is None) or (self.vmax is None):
            self.vmin = copy.deepcopy(point)
            self.vmax = copy.deepcopy(point)
        else:
            self.vmin.x = min(point.x, self.vmin.x)
            self.vmin.y = min(point.y, self.vmin.y)
            self.vmin.z = min(point.z, self.vmin.z)
            self.vmax.x = max(point.x, self.vmax.x)
            self.vmax.y = max(point.y, self.vmax.y)
            self.vmax.z = max(point.z, self.vmax.z)
