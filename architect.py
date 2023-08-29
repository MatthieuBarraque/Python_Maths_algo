import sys
import math

def Translation(i, j, x, y):
    print("Translation along vector", "(%.f," %int(i),"%.f)" %int(j))

def Scaling(a, b, x, y) :
    print("Scaling by factors", int(a), "and", int(b))

def Rotation(alpha, x, y) :
    print("Rotation by a", int(alpha), "degree angle")

def Reflection(alpha, x, y) :
    print("Reflection over an axis with an inclination angle of", int(alpha), "degrees")

def algo() :
    try :
        x = sys.argv[1]
        y = sys.argv[2]
        valuex = int(x)
        valuey = int(y)
    except IndexError :
        sys.exit(84)

    vector = [1.00, 0.00, 0.00,
               0.00, 1.00, 0.00,
               0.00, 0.00, 1.00]
    i = 3

    for i in range(len(sys.argv)) :
        if sys.argv[i] == "-t" :
            Translation(float(sys.argv[i + 1]), float(sys.argv[i + 2]), float(x), float(y))
            vector[2] = float(sys.argv[i + 1]) + vector[2]
            vector[5] = float(sys.argv[i + 2]) + vector[5]
        if sys.argv[i] == "-z" :
            Scaling(float(sys.argv[i + 1]), float(sys.argv[i + 2]), float(x), float(y))
            vector[0] = float(sys.argv[i + 1]) * vector[0]
            vector[4] = float(sys.argv[i + 2]) * vector[4]
        if sys.argv[i] == "-r" :
            Rotation(float(sys.argv[i + 1]), int(x), int(y))
            vector[0] = math.cos(float(sys.argv[i + 1]) / 180 * math.pi)
            vector[1] = -math.sin(float(sys.argv[i + 1]) / 180 * math.pi)
            vector[3] = math.sin(float(sys.argv[i + 1]) / 180 * math.pi)
            vector[4] = vector[0]
        if sys.argv[i] == "-s" :
            Reflection(float(sys.argv[i + 1]), int(x), int(y))
            vector[0] = math.cos(2 * float(sys.argv[i + 1]) / 180 * math.pi)
            vector[1] = math.sin(2 * float(sys.argv[i + 1]) / 180 * math.pi)
            vector[3] = math.sin(2 * float(sys.argv[i + 1]) / 180 * math.pi)
            vector[4] = -vector[0]


    print("%.2f" % vector[0], "\t%.2f" % vector[1], "\t%.2f" % vector[2])
    print("%.2f" % vector[3], "\t%.2f" % vector[4], "\t%.2f" % vector[5])
    print("%.2f" % vector[6], "\t%.2f" % vector[7], "\t%.2f" % vector[8])
    inteeger1 = vector[0] * valuex + vector[1] * valuey + vector[2]
    inteeger2 = vector[3] * valuex + vector[4] * valuey + vector[5]
    print("(%.2f," % valuex,"%.2f)" % valuey,"=> (%.2f," % inteeger1,"%.2f)" % inteeger2)

algo()