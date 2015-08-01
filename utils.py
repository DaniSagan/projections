import numpy as np
import math

def rotation_matrix(axis, angle):
    ux = axis.x
    uy = axis.y
    uz = axis.z
    c = math.cos(angle)
    s = math.sin(angle)
    return np.matrix([[c+ux**2*(1-c),    ux*uy*(1-c)-uz*s, ux*uz*(1-c)+uy*s],
                      [uy*ux*(1-c)+uz*s, c+uy**2*(1-c),    uy*uz*(1-c)-ux*s],
                      [uz*ux*(1-c)-uy*s, uz*uy*(1-c)+ux*s, c+uz**2*(1-c)]])
                      
def to_radians(degrees):
    return math.pi*degrees/180.