import itertools

import matplotlib.pyplot as plt

from geometry.view import View
import geometry.vec3 as vec3
from geometry.vec3 import Vec3
from geometry.shapes import SQUARE
from geometry import utils
from geometry.transform import *

if __name__ == '__main__':

    v = View(10)

    v.push_transforms(
        Scale(Vec3(100., 100., 100.)),
        Rotation(vec3.I, utils.deg_to_rad(-30.)),
        Translation(Vec3(0., 0., -500.)))

    p1 = v.project_point(SQUARE.vertices[1])
    p2 = v.project_point(SQUARE.vertices[0])
    p3 = v.project_point(SQUARE.vertices[3])

    plt.figure()
    plt.scatter(p2.x, p2.y, color='r', s=50)
    plt.scatter([p1.x, p3.x], [p1.y, p3.y], s=50)
    plt.axis('equal')
    plt.show(block=False)

    pl = v.get_plane(p1, p2, p3, 100, 100, utils.deg_to_rad(90.))

    v.clear_transforms()
    pp1 = v.project_point(pl.get_point(0, 0))
    pp2 = v.project_point(pl.get_point(1, 0))
    pp3 = v.project_point(pl.get_point(1, 1))
    pp4 = v.project_point(pl.get_point(0, 1))
    plt.plot([pp1.x, pp2.x, pp3.x, pp4.x, pp1.x], [pp1.y, pp2.y, pp3.y, pp4.y, pp1.y], color='red')
    plt.axis('equal')

    for i, j in itertools.product(range(-4, 5), range(-4, 5)):
        pp1 = v.project_point(pl.get_point(i, j))
        pp2 = v.project_point(pl.get_point(i+1, j))
        pp3 = v.project_point(pl.get_point(i+1, j+1))
        pp4 = v.project_point(pl.get_point(i, j+1))
        plt.plot([pp1.x, pp2.x, pp3.x, pp4.x, pp1.x], [pp1.y, pp2.y, pp3.y, pp4.y, pp1.y], color='black')
    plt.axis('equal')
    plt.show()
