class Tranform(object):
    def transform(self, point):
        return point


class Rotation(Transform):
    def __init__(self, axis, angle):
        self.axis = axis
        self.angle = angle
        
    def transform(self, point):
        return point.rotate(self.axis, self.angle)
        

class Translation(Transform):
    def __init__(self, movement):
        self.movement = movement
        
    def transform(self, point):
        return point.translate(self.movement)