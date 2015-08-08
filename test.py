from geometry.vec3 import Vec3

if __name__ == '__main__':
    v = Vec3(1, 0, 0)
    w = Vec3(0, 1, 0)
    print(Vec3.cross(v, w))
