from vec3 import Vec3

class Transform(object):
    def transform(self, point):
        return point


class Rotation(Transform):
    def __init__(self, axis, angle):
        self.axis = axis
        self.angle = angle

    def transform(self, point):
        return point.rotate(self.axis, self.angle)

    def __repr__(self):
        return '<Rotation transform. axis: {axis}, angle: {angle}>'.format(axis=self.axis, angle=self.angle)


class Translation(Transform):
    def __init__(self, movement):
        self.movement = movement

    def transform(self, point):
        return point.translate(self.movement)

    def __repr__(self):
        return '<Translation transform. movement: {movement}>'.format(movement=self.movement)


class Scale(Transform):
    def __init__(self, value):
        self.value = value

    def transform(self, point):
        return Vec3(self.value.x*point.x,
                    self.value.y*point.y,
                    self.value.z*point.z)

    def __repr__(self):
        return '<Scale transform. value: {value}>'.format(value=self.value)
