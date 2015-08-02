from view import View
from vec2 import Vec2
from vec3 import Vec3
from plane import Plane
import matplotlib.pyplot as plt
import utils
import transform
import itertools

if __name__ == '__main__':
    v = View(10)
    v.push_transform(transform.Rotation(Vec3(1., 0., 0.), utils.to_radians(-5.)))
    v.push_transform(transform.Rotation(Vec3(0., 1., 0.), utils.to_radians(-15.)))
    p1 = v.project_point(Vec3(-50., -600., -800.))
    p2 = v.project_point(Vec3(50., -600., -800.))
    p3 = v.project_point(Vec3(50., -600., -900.))

    plt.figure()
    plt.scatter([p1.x, p2.x, p3.x], [p1.y, p2.y, p3.y], s=50)
    plt.axis('equal')
    plt.show(block=False)

    pl = v.get_plane(p1, p2, p3, 100, 100, utils.to_radians(90.))

    v.pop_transform()
    v.pop_transform()
    pp1 = v.project_point(pl.get_point(0, 0))
    pp2 = v.project_point(pl.get_point(1, 0))
    pp3 = v.project_point(pl.get_point(1, 1))
    pp4 = v.project_point(pl.get_point(0, 1))
    plt.plot([pp1.x, pp2.x, pp3.x, pp4.x, pp1.x], [pp1.y, pp2.y, pp3.y, pp4.y, pp1.y], color='red')
    plt.axis('equal')

    for i, j in itertools.product(range(-4,5), range(-4,5)):
        pp1 = v.project_point(pl.get_point(i, j))
        pp2 = v.project_point(pl.get_point(i+1, j))
        pp3 = v.project_point(pl.get_point(i+1, j+1))
        pp4 = v.project_point(pl.get_point(i, j+1))
        plt.plot([pp1.x, pp2.x, pp3.x, pp4.x, pp1.x], [pp1.y, pp2.y, pp3.y, pp4.y, pp1.y], color='black')
    plt.axis('equal')
    plt.show()
