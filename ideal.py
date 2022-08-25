from math import sin, asin, pi, degrees, radians
import matplotlib.pyplot as plt
from numpy import NaN

n = 1.49 #PMMA

def idealRefraction(incidentAngle, n=1.49):
    in1 = radians(incidentAngle)
    out1 = asin(sin(in1)/n)
    return degrees(out1)

def plot():
    x = []
    y = []
    for i in range(-89,90):
        try:
            out = idealRefraction(i)
        except:
            out = NaN
        x.append(i)
        y.append(out)
    plt.plot(x,y)
    # plt.plot(x,ymulti,label = "LP=%d°(multipath)"%LP)
    # plt.scatter(x,y,label="LPV=%d°"%LPV,s = 5)
    plt.title("理想屈折面による屈折", fontname="MS Gothic")
    plt.xlabel("入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("出射角 [deg]", fontname="MS Gothic")
    plt.legend()
    plt.show()

plot()