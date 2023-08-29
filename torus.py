from sys import *
import math

def Secante(n, x0, x1):
    
    while float(abs(x1 - x0) > 10**(-n)):
        return 0

def Newton(n, x, xb):
    intervalle = 0
    while float(abs(xb - x) > 10**(-n)):
        xb = x
        intervalle = intervalle + 1
        if (10**n * x % 1) == 0:
            print("x =", x)
        else:
            print("x = %.*f" % (n, x))
        x = x - ((a4 * (x**4) + a3 * (x**3) + a2 * (x**2) + a1 * (x**1)  + a0 * (x**0)) / (((4 * a4 * x ** 3) + (3 * a3 * x ** 2) + (2 * a2 * x ** 1) + (1 * a1 * x ** 0))))

def equ4tion(x):
    res = (a4 * (x**4) + a3 * (x**3) + a2 * (x**2) + a1 * (x**1)  + a0 * (x**0 * 0))
    return res

def derive(x):
    res = (((4 * a4 * x ** 3) + (3 * a3 * x ** 2) + (2 * a2 * x ** 1) + (1 * a1 * x ** 0)))
    return res

def Bisectrice(n, xa, xb, arc, src):
    a4 = equ4tion(xb)
    while float(abs(arc - src)) > (10**(-n)):
        src = arc
        arc = (xb + xa)/ 2
        if a4 * (a4 * (arc**4) + a3 * (arc**3) + a2 * (arc**2) + a1 * (arc**1)  + a0 * (arc**0)) < 0: #erreur formule
            xa = arc
        else:
            xb = arc
        if (10**n) * arc % 1 == 0:
            print("x =", arc)
        else:
            print("x = %.*f" % (n, arc))

def error():
    print("USAGE")
    print("    ./105torus opt a0 a1 a2 a3 a4 n\n")
    print("DESCRIPTION")
    print("    opt       method option:")
    print("                  1 for the bisection method")
    print("                  2 for Newton’s method")
    print("                  3 for the secant method")
    print("    a[0-4] coefficients of the equation")
    print("    n      precision (the application of the polynomial to the solution should")
    print("           be smaller than 10ˆ-n)")

def main(argv):

    if len(argv) == 2 and argv[1] == "-h":
        error()
        exit (84)
    if argv[1] != "1" and argv[1] != "2" and argv[1] != "3":
        error()
        exit (84)

main(argv)

opt = int(argv[1])
a0  = int(argv[2])
a1  = int(argv[3])
a2  = int(argv[4])
a3  = int(argv[5])
a4  = int(argv[6])
n   = int(argv[7])
xa = 1
xb = 0
arc = 0
src = 1
x = 0.5 #intervalle c newton methode
x0 = 0
x1 = 1

if opt == 1:
    Bisectrice(n, xa, xb, arc, src)
if opt == 2:
    Newton(n, x, xb)
if opt == 3:
    Secante(n, x0, x1)