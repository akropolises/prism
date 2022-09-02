from math import sin, asin, pi, degrees, radians
import matplotlib.pyplot as plt
from numpy import NaN

"""n:BK7 1.51~1.53"""
def prism(incidentAngle_deg, n = 1.52, mittyaku = False, siten = False):
    assert(-90<incidentAngle_deg<90)
    isMinus = incidentAngle_deg < 0
    in1 = abs(radians(incidentAngle_deg))
    # 完全密着時視点側
    if siten and mittyaku:
        out1 = in1
    else:
        #1*sin(in1) = n*sin(out1)
        out1 = asin(sin(in1)/n)
    if isMinus:
        assert(out1<pi/4)
        in2 = pi/4 + out1
        in2isMinus = True
    else:
        in2 = abs(pi/4 - out1)
        in2isMinus = out1 < pi/4
    #n*sin(in2) = 1*sin(out2)
    if mittyaku and not siten:
        return degrees(in2)*((-1)**in2isMinus)
    try:
        out2 = asin(n*sin(in2))
        return degrees(out2)*((-1)**in2isMinus)
    except:
        return NaN

ns = [1.33,1.4,1.52]
def plot_ASKA3D(mittyaku = False):
    for n in ns:
        x = []
        y = []
        for i in range(-89,90):
            out = prism(i,n=n,mittyaku=mittyaku)
            # if -65<=out<=-25:
            #     print(i)
            x.append(i)
            y.append(out)
        plt.plot(x,y,label="n=%.2f"%n)
    plt.plot([-90,90],[-65,-65], color = "orange")
    plt.plot([-90,90],[-25,-25], color = "orange")
    if mittyaku:
        plt.title("微小空気層なし（完全密着）", fontname="MS Gothic")
    else:
        plt.title("微小空気層あり", fontname="MS Gothic")
    plt.xlabel("直角プリズム入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("ASKA3D入射角 [deg]", fontname="MS Gothic")
    plt.ylim(-90,0)
    plt.legend()
    plt.show()

def plot(mittyaku = False,recommend = False):
    for n in ns:
        x = []
        y = []
        for i in range(-89,90):
            try:
                out = prism(i,n=n,mittyaku=mittyaku)
                if recommend:
                    if -65<=out<=-25:
                        out = prism(-out,n=n,mittyaku=mittyaku,siten=True)
                    else:
                        out = NaN
                else:
                    out = prism(-out,n=n,mittyaku=mittyaku,siten=True)
            except:
                out = NaN
            x.append(i)
            y.append(out)
        plt.plot(x,y,label="n=%.2f"%n)
    titleMit = "微小空気層なし（完全密着）" if mittyaku else "微小空気層あり"
    titleRec = " 推奨入射角のみ採用" if recommend else ""
    plt.title(titleMit+titleRec, fontname="MS Gothic")
    plt.xlabel("直角プリズム入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("視域(直角プリズム出射角) [deg]", fontname="MS Gothic")
    plt.xlim(-90,90)
    plt.ylim(-90,90)
    plt.legend()
    plt.show()

def main():
    # plot_ASKA3D(mittyaku=False)
    # plot_ASKA3D(mittyaku=True)
    plot(mittyaku=False)
    plot(mittyaku=True)
    plot(mittyaku=False,recommend=True)
    plot(mittyaku=True,recommend=True)

if __name__ == "__main__":
    main()