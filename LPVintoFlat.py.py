from math import sin, asin, pi, degrees, radians
import matplotlib.pyplot as plt
from numpy import NaN

n = 1.49 #PMMA

def LPV_into_flat(incidentAngle_degree,LPV=90):
    assert(-90<incidentAngle_degree<90)
    isMinus = incidentAngle_degree<0
    in1 = abs(radians(incidentAngle_degree))
    LPV = radians(LPV)
    #1*sin(in1) = n*sin(out1)
    out1 = asin(sin(in1)/n)
    ret = []
    if isMinus:
        if out1 < LPV/2:
            #平行側
            in2 = pi/2 + out1 - LPV/2
            try:
                out2 = asin(n*sin(in2))
                out = pi/2 - (LPV/2 + out2)
                ret.append(degrees(out))
            except:
                pass
        isMinus2 = out1 + LPV/2 > pi/2
        in2 = pi/2 - out1 - LPV/2 #負もある
        try:
            out2 = asin(n*sin(in2))
            out = (pi/2 - LPV/2) - out2
            ret.append(degrees(out))
        except:
            pass
    else:
        if out1 < LPV/2:
            #平行側
            in2 = pi/2 + out1 - LPV/2
            try:
                out2 = asin(n*sin(in2))
                out = pi/2 - (LPV/2 + out2)
                ret.append(degrees(out))
            except:
                pass
        isPlus2 = out1 + LPV/2 > pi/2
        in2 = out1 + LPV/2 - pi/2 #負もある
        try:
            out2 = asin(n*sin(in2))
            out = pi/2 - LPV/2 + out2
            ret.append(degrees(out))
        except:
            pass
    #n*sin(in2) = 1*sin(out2)
    return ret

def plot():
    LPVs = [40,45,60,65,70,75,90,130,140,160]
    for LPV in LPVs:
        x = []
        y = []
        # ymulti = []
        for i in range(-89,90):
            try:
                out = LPV_into_flat(i,LPV=LPV)
            except:
                out = []
            for j in out:
                x.append(i)
                y.append(j)
        # plt.plot(x,y,label = "LP=%d°"%LP)
        # plt.plot(x,ymulti,label = "LP=%d°(multipath)"%LP)
        plt.scatter(x,y,label="LPV=%d°"%LPV,s = 5)
    plt.title("プリズムシートLPV平面から入射", fontname="MS Gothic")
    plt.xlabel("プリズムシート入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("プリズムシート出射角 [deg]", fontname="MS Gothic")
    plt.legend()
    plt.show()
plot()