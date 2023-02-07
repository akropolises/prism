from math import sin, asin, pi, degrees, radians
import matplotlib.pyplot as plt
from numpy import NaN
from ideal import idealRefractionIn

n = 1.49 #PMMA

def LPV_into_flat(incidentAngle_degree,LPV=90):
    assert(-90<incidentAngle_degree<90)
    LPV = radians(LPV)
    ret = []
    in1 = radians(incidentAngle_degree)
    out1 = asin(sin(in1)/n)
    if out1 > -LPV/2: #左斜面
        in2 = out1 - (pi/2 - LPV/2)
        try:
            out2 = asin(n*sin(in2))
            out = out2 + pi/2 - LPV/2
            ret.append(degrees(out))
        except:
            pass
    if out1 < LPV/2: # 右斜面
        in2 = pi/2 - LPV/2 + out1
        try:
            out2 = asin(n*sin(in2))
            out = out2 - (pi/2 - LPV/2)
            ret.append(degrees(out))
        except:
            pass
    return ret

def plot():
    LPVs = [40,45,60,65,70,75,90,130,140,160]
    for LPV in LPVs:
        x = []
        y = []
        for i in range(-89,90):
            out = LPV_into_flat(i,LPV=LPV)
            for j in out:
                x.append(i)
                y.append(j)
        # plt.scatter(x,y,label="LPV=%d°"%LPV,s = 5)
        plt.scatter(x,y,label="%d°"%LPV,s = 5)
    # plt.title("プリズムシートLPV平面から入射", fontname="MS Gothic")
    plt.xlabel("プリズムシート入射角 [deg]", fontname="MS Gothic", fontsize = 14)
    plt.ylabel("プリズムシート出射角 [deg]", fontname="MS Gothic", fontsize = 14)
    plt.xlim(-90,90)
    plt.ylim(-90,90)

    # x = []
    # y = []
    # for i in range(-89,90):
    #     try:
    #         out = idealRefractionIn(i)
    #     except:
    #         out = NaN
    #     x.append(i)
    #     y.append(out)
    # plt.plot(x,y, label = "ideal")
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot()