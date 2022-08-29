from math import sin, asin, pi, degrees, radians
import matplotlib.pyplot as plt
from numpy import NaN

n = 1.49 #PMMA

def LP_outfrom_flat(incidentAngle_degree,LP=40):
    assert(-90<incidentAngle_degree<90)
    in0 = radians(incidentAngle_degree)
    LP = radians(LP)
    ret = []
    if in0 < pi/2 - LP: #斜面
        in1 = in0 + LP
        out1 = asin(sin(in1)/n)
        if out1 > -(pi/2 - LP): # 平面
            in2 = out1 - LP
            try:
                out = asin(n*sin(in2))
                ret.append(degrees(out))
            except:
                pass
        if out1 < LP: # 壁
            in2 = LP-out1
            try:
                out = asin(n*sin(in2))
                ret.append(degrees(out))
            except:
                pass
    if in0 > 0: # 壁
        in1 = pi/2 - in0
        out1 = asin(sin(in1)/n)
        in2 = pi/2 - out1
        try:
            out = asin(n*sin(in2))
            ret.append(degrees(out))
        except:
            pass
    return ret

def plot():
    LPs = [15,23,25,30,40]
    for LP in LPs:
        x = []
        y = []
        for i in range(-89,90):
            try:
                out = LP_outfrom_flat(i,LP=LP)
            except:
                out = []
            for j in out:
                x.append(i)
                y.append(j)
        plt.scatter(x,y,label="LP=%d°"%LP,s = 5)
    plt.title("プリズムシートLP平面から出射", fontname="MS Gothic")
    plt.xlabel("プリズムシート入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("プリズムシート出射角 [deg]", fontname="MS Gothic")
    plt.xlim(-90,90)
    plt.ylim(-90,90)
    plt.legend()
    plt.show()
# plot()