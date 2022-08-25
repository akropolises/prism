from math import sin, asin, pi, degrees, radians
import matplotlib.pyplot as plt
from numpy import NaN

n = 1.49 #PMMA

"""
Todo
isPlus で incidentAngle < 90-LP
斜辺に入射
"""
def LP_outfrom_flat(incidentAngle_degree,LP=40):
    assert(-90<incidentAngle_degree<90)
    isMinus = incidentAngle_degree<0
    if isMinus:
        in1isMisus = -incidentAngle_degree > LP
        in1 = radians(abs(LP-(-incidentAngle_degree)))
    else:
        in1 = radians(90-incidentAngle_degree)
    LP = radians(LP)
    #1*sin(in1) = n*sin(out1)
    out1 = asin(sin(in1)/n)
    in2multi = NaN
    ret = []
    if isMinus:
        if in1isMisus:
            if out1 > pi/2 - LP:
                in2 = NaN
            else:
                in2 = out1 + LP
                "maltipath"
                out1multi = pi/2 - (LP + out1)
                in2multi = pi/2 - out1multi
                in2isMinusmulti = False
            in2isMinus = True
        else:
            in2 = abs(LP-out1)
            in2isMinus = out1 < LP
            if out1 < LP:
                "maltipath"
                out1multi = pi/2-LP+out1
                in2multi = pi/2 - out1multi
                in2isMinusmulti = False
    else:
        in2 = pi/2 - out1
        in2isMinus = False
        if out1 < LP:
            "maltipath"
            #隣に入射は考えない
            out1multi = pi/2-LP+out1
            in2multi = abs(LP-out1multi)
            in2isMinusmulti = out1multi < LP
    #n*sin(in2) = 1*sin(out2)
    try:
        out2 = asin(n*sin(in2))
        ret.append(degrees(out2)*((-1)**in2isMinus))
    except:
        pass
    try:
        out2multi = asin(n*sin(in2multi))
        ret.append(degrees(out2multi)*((-1)**in2isMinusmulti))
    except:
        pass
    if not isMinus and LP + radians(incidentAngle_degree) < pi/2:
        "tokusyu"
        in1 = LP + radians(incidentAngle_degree)
        out1 = asin(sin(in1)/n)
        in2 = abs(LP-out1)
        in2isMinus = out1 < LP
        if out1 < LP:
            "maltipath"
            out1multi = pi/2-LP+out1
            in2multi = pi/2 - out1multi
            in2isMinusmulti = False
        else:
            in2multi = NaN
        try:
            out2 = asin(n*sin(in2))
            ret.append(degrees(out2)*((-1)**in2isMinus))
        except:
            pass
        try:
            out2multi = asin(n*sin(in2multi))
            ret.append(degrees(out2multi)*((-1)**in2isMinusmulti))
        except:
            pass
    return ret

def plot():
    LPs = [15,23,25,30,40]
    for LP in LPs:
    # for LP in [40]:
        x = []
        y = []
        ymulti = []
        for i in range(-89,90):
            try:
                out = LP_outfrom_flat(i,LP=LP)
            except:
                out = []
            for j in out:
                x.append(i)
                y.append(j)
            # ymulti.append(out[1])
        # plt.plot(x,y,label = "LP=%d°"%LP)
        # plt.plot(x,ymulti,label = "LP=%d°(multipath)"%LP)
        plt.scatter(x,y,label="LP=%d°"%LP,s = 5)
    plt.title("プリズムシートLP平面から出射", fontname="MS Gothic")
    plt.xlabel("プリズムシート入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("プリズムシート出射角 [deg]", fontname="MS Gothic")
    plt.legend()
    plt.show()
# plot()