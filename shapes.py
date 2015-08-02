from vec3 import Vec3
from vec2 import Vec2

class LineStripe(object):
    def __init__(self, vertices, indices):
        self.vertices = vertices
        self.indices = indices

    def get_vertices(self):
        return [self.vertices[i] for i in self.indices]

    def __repr__(self):
        return str(self.get_vertices())

class Shape(object):
    def __init__(self, vertices, index_lists):
        self.vertices = vertices
        self.index_lists = index_lists

    def get_lines(self):
        return [LineStripe(self.vertices, index_list) for index_list in self.index_lists]

SQUARE = Shape([Vec3(-0.5, -0.5, 0.), Vec3(0.5, -0.5, 0.), Vec3(0.5, 0.5, 0.), Vec3(-0.5, 0.5, 0.)], [[0, 1, 2, 3, 0]])
CUBE = Shape([Vec3(-0.5, -0.5, -0.5), Vec3(0.5, -0.5, -0.5), Vec3(0.5, 0.5, -0.5), Vec3(-0.5, 0.5, -0.5),
              Vec3(-0.5, -0.5, 0.5), Vec3(0.5, -0.5, 0.5), Vec3(0.5, 0.5, 0.5), Vec3(-0.5, 0.5, 0.5)],
             [[0, 1, 2, 3, 0], [4, 5, 6, 7, 4], [0, 4], [1, 5], [2, 6], [3, 7]])
