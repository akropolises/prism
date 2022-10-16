from ideal import idealRefractionOut
from right_angle_prism import prism
from LPintoFlat import LP_into_flat
from LPoutfromFlat import LP_outfrom_flat
from math import asin, sin, radians, degrees, isnan
import matplotlib.pyplot as plt

def non():
    return [(-65,-25), (25,65)]

def idealver(deg=45, n=1.49):
    assert(0<=deg<=180)
    ret = []
    if -65+deg <= 90:
        out_mm = -65+deg
        out_mM = min(-25+deg,90)
        in_mm = idealRefractionOut(out_mm, n=n)
        in_mM = idealRefractionOut(out_mM, n=n)
        if not (isnan(in_mm) or isnan(in_mM)):
            ret.append((in_mm-deg, in_mM-deg))
    if 25+deg <= 90:
        out_pm = 25+deg
        out_pM = min(65+deg,90)
        in_pm = idealRefractionOut(out_pm, n=n)
        in_pM = idealRefractionOut(out_pM, n=n)
        if not (isnan(in_pM) or isnan(in_pM)):
            ret.append((in_pm-deg, in_pM-deg))
    return ret

def test():
    r = idealver(45, n=1.51)
    for i in r:
        assert(-78<=i[0]<=-76)
        assert(-14<=i[1]<=-12)

def LP_minus(deg = 45, LP = 40):
    assert(0<=deg<=180)
    ret = []
    if -65+deg <= 90:
        out_mm = -65+deg
        out_mM = min(-25+deg,90)
        try:
            in_mm = LP_into_flat(-out_mm, LP=LP) # 裏から入れる時はマイナスdeg
            in_mM = LP_into_flat(-out_mM, LP=LP)
            for i in in_mm:
                for j in in_mM:
                    ret.append((-i-deg,-j-deg))
        except:
            pass
    return ret

def LP_plus(deg = 45, LP=40):
    assert(0<=deg<=180)
    ret = []
    if 25+deg <= 90:
        out_pm = 25+deg
        out_pM = min(65+deg,90)
        try:
            in_pm = LP_into_flat(-out_pm, LP=LP)
            in_pM = LP_into_flat(-out_pM, LP=LP)
            for i in in_pm:
                for j in in_pM:
                    ret.append((-i-deg,-j-deg))
        except:
            pass
    return ret

def LP_45minus(deg = 45, LP=40):
    assert(0<=deg<=180)
    ret = []
    if -45+deg <= 90:
        out_m = -45+deg
        try:
            in_m = LP_into_flat(-out_m, LP=LP) # 裏から入れる時はマイナスdeg
            for i in in_m:
                ret.append(-i-deg)
        except:
            pass
    return ret

def LP_45plus(deg = 45, LP=40):
    assert(0<=deg<=180)
    ret = []
    if 45+deg <= 90:
        out_m = 45+deg
        try:
            in_m = LP_into_flat(-out_m, LP=LP) # 裏から入れる時はマイナスdeg
            for i in in_m:
                ret.append(-i-deg)
        except:
            pass
    return ret

def plot(LP=40):
    plt.rcParams["font.family"] = "MS Gothic"
    x = []
    yOver = []
    yUnder = []
    for deg in range(91):
        r = LP_minus(deg, LP)
        for i in r:
            x.append(deg)
            yOver.append(i[1])
            yUnder.append(i[0])
            
            #test
            for incident in i:
                in1 = incident + deg
                out1 = LP_outfrom_flat(in1,LP=LP)
                if out1:
                    # print(out1[0] - deg,incident)
                    assert((24 <= abs(out1[0]-deg) <= 26) or (64 <= abs(out1[0]-deg) <= 66))
    plt.plot(x,yOver, label=-25)
    plt.plot(x,yUnder,label=-65)

    x = []
    yOver = []
    yUnder = []
    for deg in range(91):
        r = LP_plus(deg, LP)
        for i in r:
            x.append(deg)
            yOver.append(i[1])
            yUnder.append(i[0])
            
            #test
            for incident in i:
                in1 = incident + deg
                out1 = LP_outfrom_flat(in1, LP=LP)
                if out1:
                    # print(out1[0] - deg,incident)
                    assert((24 <= abs(out1[0]-deg) <= 26) or (64 <= abs(out1[0]-deg) <= 66))
    if yOver:
        plt.plot(x,yOver, label=65)
        plt.plot(x,yUnder,label=25)
    
    x = []
    y = []
    for deg in range(91):
        r = LP_45minus(deg, LP=LP)
        for i in r:
            x.append(deg)
            y.append(i)
            
            #test
            in1 = i + deg
            out1 = LP_outfrom_flat(in1, LP=LP)
            if out1:
                assert(44 <= abs(out1[0]-deg) <= 46)
    plt.plot(x,y, label=-45)

    x = []
    y = []
    for deg in range(91):
        r = LP_45plus(deg, LP=LP)
        for i in r:
            x.append(deg)
            y.append(i)
            
            #test
            in1 = i + deg
            out1 = LP_outfrom_flat(in1, LP=LP)
            if out1:
                assert(44 <= abs(out1[0]-deg) <= 46)
    if y:
        plt.plot(x,y, label=45)

    plt.title("屈折回数とRT Plate入射角の関係 LP%d"%LP, fontname="MS Gothic")
    plt.xlabel("RT Plateとプリズムシートの成す角 [deg]", fontname="MS Gothic")
    plt.ylabel("プリズムシート入射角（RT Plate基準） [deg]", fontname="MS Gothic")
    plt.xlim(0,90)
    # plt.ylim(-90,90)
    plt.legend()
    plt.show()

def plot_all(LP=40):
    for deg in range(90):
        for inc in range(-90,90):
            if not (-90<inc+deg<90):
                continue
            out = LP_outfrom_flat(inc + deg, LP=LP)
            if out:
                in_ = []
                try:
                    in_ = LP_into_flat(-out[0], LP=LP)
                except:
                    print(deg,inc)
                    continue
                    pass
                for j in in_:
                    assert(abs(-j-deg-inc) < 1)
                if 25 <= abs(out[0]-deg) <= 65:
                    if -66 <= out[0]-deg <= -64:
                        plt.plot(deg,inc,marker='.', c="tab:orange")
                    elif -26 <= out[0]-deg <= -24:
                        plt.plot(deg,inc,marker='.', c="tab:blue")
                    elif -46 <= out[0]-deg <= -44:
                        plt.plot(deg,inc,marker='.', c="tab:purple")
                    else:
                        plt.plot(deg,inc,marker='.', c="tab:green")
    plt.xlabel("RT Plateとプリズムシートの成す角 [deg]", fontname="MS Gothic")
    plt.ylabel("プリズムシート入射角（RT Plate基準） [deg]", fontname="MS Gothic")
    plt.xlim(0,90)
    plt.show()

if __name__ == "__main__":
    test()
    # plot(40)
    plot_all()

    # incident, deg = (-10,20)
    # in1 = incident + deg
    # out1 = LP_outfrom_flat(in1)
    # print(out1[0] - deg)