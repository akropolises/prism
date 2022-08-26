from math import sin, asin, pi, degrees, radians
import matplotlib.pyplot as plt
from numpy import NaN

n = 1.49 #PMMA

def idealRefractionIn(incidentAngle, n=1.49):
    in1 = radians(incidentAngle)
    out1 = asin(sin(in1)/n)
    return degrees(out1)

def idealRefractionOut(incidentAngle, n=1.49):
    in1 = radians(incidentAngle)
    out1 = asin(n*sin(in1))
    return degrees(out1)

def plot(mode = "in"):
    x = []
    y = []
    for i in range(-89,90):
        try:
            if mode == "in":
                out = idealRefractionIn(i)
            else:
                out = idealRefractionOut(i)
        except:
            out = NaN
        x.append(i)
        y.append(out)
    plt.plot(x,y)
    # plt.plot(x,ymulti,label = "LP=%d°(multipath)"%LP)
    # plt.scatter(x,y,label="LPV=%d°"%LPV,s = 5)
    if mode == "in":
        plt.title("理想屈折面による屈折入射", fontname="MS Gothic")
    else:
        plt.title("理想屈折面による屈折出射", fontname="MS Gothic")
    plt.xlabel("入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("出射角 [deg]", fontname="MS Gothic")
    plt.xlim(-90,90)
    plt.ylim(-90,90)
    plt.legend()
    plt.show()

# plot(mode="out")