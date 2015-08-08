from __future__ import print_function

import matplotlib.pyplot as plt

from geometry.vec3 import Vec3
from geometry.vec2 import Vec2
from geometry.view import View
from geometry import shapes, transform
from geometry.shapes import LineStripe

if __name__ == '__main__':
    v = View(100)
    l = LineStripe([Vec3(0., 0., 0.), Vec3(100., 0., 0.)], [0, 1])
    ship = shapes.Shape.load('assets/low_poly_express_ship.obj')

    plt.figure('projection')
    for k in range(1):
        for line in ship.get_lines():
            v.push_transform(transform.Translation(Vec3(0, 0, -1000)))
            plt.plot(*Vec2.get_xy_lists(v.project_line(line)), color='k')
            v.pop_transform()
    plt.axis('equal')
    plt.show()
