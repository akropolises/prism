from math import sin, asin, pi, degrees, radians
import matplotlib.pyplot as plt
from numpy import NaN

n = 1.49 #PMMA

def LP_into_flat(incidentAngle_degree,LP=40):
    assert(-90<incidentAngle_degree<90)
    isMinus = incidentAngle_degree<0
    in1 = radians(incidentAngle_degree)*((-1)**isMinus)
    LP = radians(LP)
    #1*sin(in1) = n*sin(out1)
    out1 = asin(sin(in1)/n)
    ret = []
    if isMinus:
        if pi/2 - out1 > LP:
            try:
                in2 = LP + out1
                out2 = asin(n*sin(in2))
                out = LP-out2 #正負が正しい
                ret.append(degrees(out))
            except:
                pass
        ret += kabe(out1,LP)
    else:
        ret.append(out1isPlus(out1,LP))
    #n*sin(in2) = 1*sin(out2)
    return ret

def out1isPlus(out1, LP):
    in2 = abs(LP-out1)
    in2isMinus = out1 < LP
    out2 = asin(n*sin(in2))
    if in2isMinus:
        out = LP-out2 #負で正しい
    else:
        out = LP+out2 #正で正しい
        assert(out<pi/2) #隣の絶壁にぶつかるのは考えない
    return degrees(out)
def kabe(out1,LP):
    ret = []
    try:
        in2 = pi/2 - out1
        out2 = asin(n*sin(in2))
        out = out2 - pi/2 #負で正しい
        ret.append(degrees(out))
    except:
        pass
    try:
        ret.append(out1isPlus(out1,LP))
    except:
        pass
    return ret

def plot():
    LPs = [15,23,25,30,40]
    for LP in LPs:
        x = []
        y = []
        # ymulti = []
        for i in range(-89,90):
            try:
                out = LP_into_flat(i,LP=LP)
            except:
                out = []
            for j in out:
                x.append(i)
                y.append(j)
        # plt.plot(x,y,label = "LP=%d°"%LP)
        # plt.plot(x,ymulti,label = "LP=%d°(multipath)"%LP)
        plt.scatter(x,y,label="LP=%d°"%LP,s = 5)
    plt.title("プリズムシートLP平面から入射", fontname="MS Gothic")
    plt.xlabel("プリズムシート入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("プリズムシート出射角 [deg]", fontname="MS Gothic")
    plt.legend()
    plt.show()
# plot()