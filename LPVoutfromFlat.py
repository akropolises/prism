from math import sin, asin, pi, degrees, radians
import matplotlib.pyplot as plt
from numpy import NaN

n = 1.49 #PMMA

def LPV_outfrom_flat(incidentAngle_degree,LPV=40):
    assert(-90<incidentAngle_degree<90)
    isMinus = incidentAngle_degree<0
    in0 = abs(radians(incidentAngle_degree))
    LPV = radians(LPV)
    ret = []
    if isMinus:
        if in0 < LPV/2:
            in1 = in0 + pi/2 - LPV/2
            out1 = asin(sin(in1)/n)
            in2 = pi/2 - (out1 + LPV/2)
            out = asin(n*sin(in2))
            ret.append(degrees(out))
        pass
    else:
        if in0 < LPV/2:
            pass
        pass
    return ret

def plot():
    LPVs = [40,45,60,65,70,75,90,130,140,160]
    for LPV in LPVs:
        x = []
        y = []
        for i in range(-89,90):
            try:
                out = LPV_outfrom_flat(i,LPV=LPV)
            except:
                out = []
            for j in out:
                x.append(i)
                y.append(j)
            # ymulti.append(out[1])
        # plt.plot(x,y,label = "LP=%d°"%LP)
        # plt.plot(x,ymulti,label = "LP=%d°(multipath)"%LP)
        plt.scatter(x,y,label="LPV=%d°"%LPV,s = 5)
    plt.title("プリズムシートLPV平面から出射", fontname="MS Gothic")
    plt.xlabel("プリズムシート入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("プリズムシート出射角 [deg]", fontname="MS Gothic")
    plt.legend()
    plt.show()
# plot()