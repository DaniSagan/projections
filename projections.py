from __future__ import print_function
from vec3 import Vec3
from vec2 import Vec2
from view import View
from line import Line, Direction
from view import View
import shapes
from shapes import LineStripe
import transform
import utils
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random

if __name__ == '__main__':
    v = View(100)
    l = LineStripe([Vec3(0.,0.,0.), Vec3(100.,0.,0.)], [0, 1])
    ship = shapes.Shape.load('low_poly_express_ship.obj')

    plt.figure('projection')
    for k in range(1):
        for line in ship.get_lines():
            v.push_transform(transform.Translation(Vec3(0,0,-1000)))
            plt.plot(*Vec2.get_xy_lists(v.project_line(line)), color='k')
            v.pop_transform()
    plt.axis('equal')
    plt.show()
