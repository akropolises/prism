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

def plotWithASKA3D(recommend=False):
    x = []
    y = []
    ranges = [i/10 for i in range(-899,900)]
    for i in ranges:
        tmp = idealRefractionIn(i)
        before = tmp-45
        after = -before
        j = after-45
        if recommend:
            if -65 <= before <= -25 or 25 <= before <= 65:
                try:
                    out = idealRefractionOut(j)
                except:
                    out = NaN
            else:
                out = NaN
        else:
            try:
                out = idealRefractionOut(j)
            except:
                out = NaN
        x.append(i)
        y.append(out)
    plt.plot(x,y)
    title = "理想屈折面による屈折"
    titleRec = " 推奨入射角のみ採用" if recommend else ""
    plt.title(title+titleRec, fontname="MS Gothic")
    plt.xlabel("光源側屈折面入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("視点側屈折面出射角 [deg]", fontname="MS Gothic")
    plt.xlim(-90,90)
    plt.ylim(-90,90)
    plt.legend()
    plt.show()

# plotWithASKA3D()
# plotWithASKA3D(recommend=True)