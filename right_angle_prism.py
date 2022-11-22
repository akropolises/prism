from math import radians, degrees, sin, asin, pi, acos, tan
import matplotlib.pyplot as plt

"""RT Plateに平行な面を通る光路"""
def prism1(incidentAngle_deg, n = 1.52):
    assert(-90<incidentAngle_deg<90)
    in1 = radians(incidentAngle_deg)
    out1 = asin(sin(in1)/n)
    if out1 <= -pi/4:
        return
    in2 = out1 - pi/4
    try:
        out2 = asin(n*sin(in2))
        return degrees(out2)
    except:
        return

"""RT Plateに垂直な面を通る光路"""
def prism2(incidentAngle_deg, n = 1.52, siten = False):
    assert(-90<incidentAngle_deg<90)
    in1 = radians(incidentAngle_deg)
    out1 = asin(sin(in1)/n)
    if out1 >= pi/4:
        return
    in2 = out1 + pi/4
    try:
        out2 = asin(n*sin(in2))
        if siten:
            return degrees(out2)
        deg = degrees(out2) - 90
        if -90<deg<90:
            return deg
        else:
            return
    except:
        return

def test():
    for i in range(-89,90):
        i1 = prism1(i)
        if i1 is None:
            continue
        i2 = prism1(-i1)
        assert(abs(i+i2)<0.01)
    for i in range(-89,90):
        i1 = prism2(i)
        if i1 is None:
            continue
        i2 = prism2(-i1-90,siten=True)
        assert(abs(i+i2)<0.01)

"""横軸が直角プリズムの斜辺に対する方位角"""
def plot_ASKA3D():
    x = []
    y1 = []
    y2 = []
    for i in range(-89,90):
        out1 = prism1(i)
        out2 = prism2(i)
        x.append(i)
        y1.append(out1)
        y2.append(out2)
    plt.plot(x,y1, label = "RT Plateに密着した面")
    plt.plot(x,y2, label = "RT Plateに垂直な面")
    plt.plot([-90,90],[-65,-65], color = "orange")
    plt.plot([-90,90],[-25,-25], color = "orange")
    plt.title("直角プリズム入射角+45°が論文における鑑賞方向", fontname="MS Gothic")
    plt.xlabel("直角プリズム入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("ASKA3D入射角 [deg]", fontname="MS Gothic")
    plt.ylim(-90,0)
    plt.legend(prop={"family":"MS Gothic"})
    plt.show()

"""横軸がRT Plateに対する方位角"""
def plot_ASKA3D2():
    x = []
    y1 = []
    y2 = []
    for i in range(-89,90):
        out1 = prism1(i)
        out2 = prism2(i)
        x.append(i+45)
        y1.append(out1)
        y2.append(out2)
    plt.plot(x,y1, label = "RT Plateに密着した面")
    plt.plot(x,y2, label = "RT Plateに垂直な面")
    plt.plot([-45,135],[-65,-65], color = "orange")
    plt.plot([-45,135],[-25,-25], color = "orange")
    theory_20 = 18.2
    theory_70 = 71.8
    plt.plot([theory_20,theory_20],[-45,-90], color = "tab:green")
    plt.plot([theory_70,theory_70],[-45,-90], color = "tab:green")
    plt.plot([0,theory_70],[-45,-45], color = "tab:green")
    plt.xlabel("鑑賞方向 [deg]", fontname="MS Gothic")
    plt.ylabel("ASKA3D入射角 [deg]", fontname="MS Gothic")
    plt.xlim(0,90)
    plt.ylim(-90,0)
    plt.legend(prop={"family":"MS Gothic"})
    plt.show()

"""RT Plate+直角プリズム2つ"""
def withRTPlate(mode:str, condition:int, recommend = False):
    assert(mode in {"I","W","X","Y"})
    assert(condition in {1,2})
    theta = []
    phi = []

    for theta_in in range(-89,90):
        thetaASKAin = prism1(theta_in) if condition == 1 else prism2(theta_in)
        if thetaASKAin is None:
            continue
        if not (-90 < thetaASKAin < 90):
            continue
        for phi_in in range(-89,90):
            phiASKAin = phi_in
            if recommend:
                thetaR = radians(thetaASKAin)
                phiR = radians(phiASKAin)
                psi = 90 - degrees(acos(1/(tan(thetaR)**2 + tan(phiR)**2 + 1)**(1/2)))
                if mode == "I":
                    if not (25 <= psi <= 65):
                        continue
                else:
                    if 25 <= psi <= 65:
                        continue
            ASKAdict = {"I":(-thetaASKAin, -phiASKAin), "W":(thetaASKAin, phiASKAin), "X":(phiASKAin, thetaASKAin), "Y":(-phiASKAin, -thetaASKAin)}
            thetaASKAout, phiASKAout = ASKAdict[mode]
            try:
                theta_out = prism1(thetaASKAout) if condition == 1 else prism2(thetaASKAout-90,siten=True)
            except:
                continue
            if theta_out is None:
                continue
            assert(-90 < theta_out < 90)
            phi_out = phiASKAout
            theta.append((theta_out + 45))
            phi.append(phi_out)
    return theta, phi

"""視域の可視化"""
def plot_viewangle(condition:int, mode:str="A",  recommend = False):
    assert(mode in {"I","W","X","Y","A"})
    assert(condition in (1,2,3))
    labeldict = {"W":"両側透過光", "X":"X側透過光", "Y":"Y側透過光", "I":"結像光"}
    colordict = {"I":"tab:blue", "W":"tab:orange", "X":"tab:green", "Y":"tab:red"}
    if mode != "A":
        if condition == 3:
            x,y = withRTPlate(mode, 1, recommend=recommend)
            plt.scatter(x, y, label=labeldict[mode], s=5, c=colordict[mode])
            x,y = withRTPlate(mode, 2, recommend=recommend)
            plt.scatter(x, y, s=5, c=colordict[mode])
        else:
            x,y = withRTPlate(mode, condition, recommend=recommend)
            plt.scatter(x, y, label=labeldict[mode], s=5, c=colordict[mode])
    else:
        if condition == 3:
            for i in ("I","W","X","Y"):
                x,y = withRTPlate(i,1,recommend=recommend)
                plt.scatter(x, y, label=labeldict[i], s=5, c=colordict[i])
            for i in ("I","W","X","Y"):
                x,y = withRTPlate(i,2,recommend=recommend)
                plt.scatter(x, y, s=5, c=colordict[i])
        else:
            for i in ("I","W","X","Y"):
                x,y = withRTPlate(i,condition,recommend=recommend)
                plt.scatter(x, y, label=labeldict[i], s=5)
    plt.xlabel("方位角 [deg]", fontname="MS Gothic")
    plt.ylabel("仰角 [deg]", fontname="MS Gothic")
    plt.xlim(-90+45,90+45)
    plt.ylim(-90,90)
    plt.legend(prop={"family":"MS Gothic"})
    plt.show()

if __name__ == "__main__":
    test()
    # plot_ASKA3D()
    # plot_ASKA3D2()
    plot_viewangle(3)


#以下は考察が不完全な時に書いたコード
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
            try:
                out = prism(i,n=n,mittyaku=mittyaku)
            except:
                continue
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

def plot_RTPlate_rec():
    # plt.rcParams["font.family"] = "MS Gothic"
    plt.plot([-90,90],[-90-45,90-45],label="0回屈折")
    x = []
    y = []
    for i in range(-89,90):
        try:
            out = prism(i,n=1.52,mittyaku=True)
        except:
            continue
        x.append(i)
        y.append(out)
    plt.plot(x,y,label="1回屈折")
    x = []
    y = []
    for i in range(-89,90):
        try:
            out = prism(i,n=1.52,mittyaku=False)
        except:
            continue
        x.append(i)
        y.append(out)
    plt.plot(x,y,label="2回屈折")
    plt.plot([-90,90],[-65,-65], color = "tab:red")
    plt.plot([-90,90],[-25,-25], color = "tab:red")
    # plt.title("屈折回数とRT Plate入射角の関係", fontname="MS Gothic")
    plt.xlabel("第一屈折面入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("RT Plate入射角 [deg]", fontname="MS Gothic")
    plt.xlim(-90,90)
    plt.ylim(-90,0)
    plt.legend(prop={"family":"MS Gothic"})
    plt.show()

def main():
    # plot_ASKA3D(mittyaku=False)
    # plot_ASKA3D(mittyaku=True)
    # plot(mittyaku=False)
    # plot(mittyaku=True)
    # plot(mittyaku=False,recommend=True)
    # plot(mittyaku=True,recommend=True)
    plot_RTPlate_rec()

# if __name__ == "__main__":
#     main()