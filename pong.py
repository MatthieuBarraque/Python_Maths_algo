from sys import argv
from math import asin, degrees, sqrt


class vector :  
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __round__(self, ndigits=2):
        return round(self.x)
        

v = vector(1, 2, 3)

def return_vector(x, y, z):
    vect = vector(x, y, z)
    return vect

def soustraction__vector(v1, v2):
    soustraction = vector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
    return soustraction

def addition__vector(v1, v2):
    addition = vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)
    return addition

def multiplication__vector(v1, m):
    multiplication = vector(v1.x*m, v1.y*m, v1.z*m)
    return multiplication

def norm__vector(v1):
    racine = sqrt(v1.x*v1.x + v1.y*v1.y + v1.z*v1.z)
    return racine

argv = [float(i) for i in argv[1:]]

x0 = argv[1-1]
y0 = argv[2-1]
z0 = argv[3-1]
x1 = argv[4-1]
y1 = argv[5-1]
z1 = argv[6-1]
n = argv[7-1]

po = vector(x0, y0, z0)
pp = vector(x1, y1, z1)
vec_dir = soustraction__vector(pp, po)
pf = addition__vector(pp, multiplication__vector(vec_dir, n))
my_str_1 = str(round(vec_dir, 2))

def alpha__vector(vec_dir):
    alpha = abs(degrees(asin(vec_dir.z/norm__vector(vec_dir))))
    return alpha

print("The velocity vector of the ball is:")
print("(%.2f," % vec_dir.x, "%.2f," % vec_dir.y, "%.2f)" % vec_dir.z)
print("At time t + 4, ball coordinates will be:")
print("(%.2f," % pf.x, "%.2f," % pf.y, "%.2f)" % pf.z)

if(vec_dir.z < 0 and z1 < 0):
    print("The ball won't reach the paddle.")
else:
        print("The incidence angle is:")
        print("%.2f degrees" % alpha__vector(vec_dir))