from math import acos,cos,degrees,sin,radians,tan
import matplotlib.pyplot as plt
from LPintoFlat import LP_into_flat
from LPoutfromFlat import LP_outfrom_flat
from LPVintoFlat import LPV_into_flat
from LPVoutfromFlat import LPV_outfrom_flat
from right_angle_prism import prism
from ideal import idealRefractionIn, idealRefractionOut

LPs = [15,23,25,30,40]
LPVs = [40,45,60,65,70,75,90,130,140,160]

def non(mode:str, deg = 45, recommend = False):
    assert(mode in {"I","W","X","Y"})
    theta = []
    phi = []

    for theta_in0 in range(-89,90):
        theta_in1 = theta_in0
        thetaASKAin = theta_in1 - deg
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
            theta_out0 = thetaASKAout - deg
            if not (-90 < theta_out0 < 90):
                if mode != "I":
                    theta.append(thetaASKAout)
                    phi.append(phiASKAout)
            else:
                theta_out1 = theta_out0
                phi_out = phiASKAout
                theta.append(theta_out1)
                phi.append(phi_out)
    return theta, phi

def LPver(mode:str, deg = 45, flatisout = True, LP = 40, recommend = False):
    assert(mode in {"I","W","X","Y"})
    theta = []
    phi = []

    for theta_in0 in range(-89,90):
        theta_in1s = LP_into_flat(theta_in0,LP=LP) if flatisout else LP_outfrom_flat(theta_in0,LP=LP)
        for theta_in1 in theta_in1s:
            thetaASKAin = theta_in1 - deg
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
                theta_out0 = thetaASKAout - deg
                if not (-90 < theta_out0 < 90):
                    continue
                    if mode != "I":
                        theta.append(thetaASKAout)
                        phi.append(phiASKAout)
                else:
                    theta_out1s = LP_outfrom_flat(theta_out0,LP=LP) if flatisout else LP_into_flat(theta_out0,LP=LP)
                    phi_out = phiASKAout
                    for theta_out1 in theta_out1s:
                        theta.append(theta_out1)
                        phi.append(phi_out)
    return theta, phi

def LPVver(mode:str, deg = 45, flatisout = True, LPV = 90, recommend = False):
    assert(mode in {"I","W","X","Y"})
    theta = []
    phi = []

    for theta_in0 in range(-89,90):
        theta_in1s = LPV_into_flat(theta_in0,LPV=LPV) if flatisout else LPV_outfrom_flat(theta_in0,LPV=LPV)
        for theta_in1 in theta_in1s:
            thetaASKAin = theta_in1 - deg
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
                theta_out0 = thetaASKAout - deg
                if not (-90 < theta_out0 < 90):
                    continue
                    if mode != "I":
                        theta.append(thetaASKAout)
                        phi.append(phiASKAout)
                else:
                    theta_out1s = LPV_outfrom_flat(theta_out0,LPV=LPV) if flatisout else LPV_into_flat(theta_out0,LPV=LPV)
                    phi_out = phiASKAout
                    for theta_out1 in theta_out1s:
                        theta.append(theta_out1)
                        phi.append(phi_out)
    return theta, phi

def prismver(mode:str, recommend = False):
    assert(mode in {"I","W","X","Y"})
    theta = []
    phi = []

    for theta_in in range(-89,90):
        thetaASKAin = prism(theta_in,siten=False)
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
            theta_out = prism(thetaASKAout,siten=True)
            if not (-90 < theta_out < 90):
                continue
                if mode != "I":
                    theta.append(thetaASKAout)
                    phi.append(phiASKAout)
            else:
                phi_out = phiASKAout
                theta.append(theta_out)
                phi.append(phi_out)
    return theta, phi

def idealver(mode:str, deg = 45, recommend = False):
    assert(mode in {"I","W","X","Y"})
    theta = []
    phi = []

    for theta_in0 in range(-89,90):
        theta_in1 = idealRefractionIn(theta_in0)
        thetaASKAin = theta_in1 - deg
        if not (-90 < thetaASKAin < 90):
            continue
        for phi_in in range(-89,90):
            phiASKAin = idealRefractionIn(phi_in)
            if not (-90 < phiASKAin < 90):
                continue
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
            theta_out0 = thetaASKAout - deg
            if not (-90 < theta_out0 < 90):
                continue
                if mode != "I":
                    theta.append(thetaASKAout)
                    phi.append(phiASKAout)
            else:
                theta_out1 = idealRefractionOut(theta_out0)
                phi_out = idealRefractionOut(phiASKAout)
                theta.append(theta_out1)
                phi.append(phi_out)
    return theta, phi



def unitPlot(mode:str, condition:str, deg = 45, flatisout = True, LP = 40, LPV = 90, recommend = False):
    assert(mode in {"I","W","X","Y"})
    assert(condition in {"non", "LP", "LPV", "prism", "ideal"})
    labeldict = {"W": "両側透過光", "X":"X側透過光", "Y":"Y側透過光", "I":"結像光"}
    colordict = {"I":"tab:blue", "W":"tab:orange", "X":"tab:green", "Y":"tab:red"}
    if condition == "non":
        x,y = non(mode,deg=deg,recommend=recommend)
        plt.scatter(x, y, label=labeldict[mode], s=5, c=colordict[mode])
        plt.title("屈折なし", fontname="MS Gothic")
    elif condition == "LP":
        x,y = LPver(mode,deg=deg,flatisout=flatisout,LP=LP,recommend=recommend)
        plt.scatter(x, y, label=labeldict[mode], s=5, c=colordict[mode])
        plt.title("LP%d"%LP, fontname="MS Gothic")
    elif condition == "LPV":
        x,y = LPVver(mode,deg=deg,flatisout=flatisout,LPV=LPV,recommend=recommend)
        plt.scatter(x, y, label=labeldict[mode], s=5, c=colordict[mode])
        plt.title("LPV%d"%LPV, fontname="MS Gothic")
    elif condition == "prism":
        x,y = prismver(mode,recommend=recommend)
        plt.scatter(x, y, label=labeldict[mode], s=5, c=colordict[mode])
        plt.title("直角プリズム", fontname="MS Gothic")
    elif condition == "ideal":
        x,y = idealver(mode,deg=deg, recommend=recommend)
        plt.scatter(x, y, label=labeldict[mode], s=5, c=colordict[mode])
        plt.title("理想状態", fontname="MS Gothic")
    plt.xlabel("方位角 [deg]", fontname="MS Gothic")
    plt.ylabel("仰角 [deg]", fontname="MS Gothic")
    plt.xlim(-90,90)
    plt.ylim(-90,90)
    plt.legend(prop={"family":"MS Gothic"})
    plt.show()


def All_mode(mode:str, deg = 45, flatisout = True, LP = 40, LPV = 90, recommend = False):
    assert(mode in {"non", "LP", "LPV", "prism", "ideal", "All"})
    labeldict = {"W": "両側透過光", "X":"X側透過光", "Y":"Y側透過光", "I":"結像光"}
    if mode in ("non", "All"):
        for i in ("I","W","X","Y"):
            x,y = non(i,deg=deg, recommend=recommend)
            plt.scatter(x, y, label=labeldict[i], s=5)
        plt.title("屈折なし", fontname="MS Gothic")
        plt.xlabel("方位角 [deg]", fontname="MS Gothic")
        plt.ylabel("仰角 [deg]", fontname="MS Gothic")
        plt.xlim(-90,90)
        plt.ylim(-90,90)
        plt.legend(prop={"family":"MS Gothic"})
        plt.show()
    if mode in ("LP", "All"):
        for i in ("I","W","X","Y"):
            x,y = LPver(i,deg=deg,flatisout=flatisout,LP=LP,recommend=recommend)
            plt.scatter(x, y, label=labeldict[i], s=5)
        plt.title("LP%d_%d"%(LP,deg), fontname="MS Gothic")
        plt.xlabel("方位角 [deg]", fontname="MS Gothic")
        plt.ylabel("仰角 [deg]", fontname="MS Gothic")
        plt.xlim(-90,90)
        plt.ylim(-90,90)
        plt.legend(prop={"family":"MS Gothic"})
        plt.show()
    if mode in ("LPV", "All"):
        for i in ("I","W","X","Y"):
            x,y = LPVver(i,deg=deg,flatisout=flatisout,LPV=LPV,recommend=recommend)
            plt.scatter(x, y, label=labeldict[i], s=5)
        plt.title("LPV%d_%d"%(LPV,deg), fontname="MS Gothic")
        plt.xlabel("方位角 [deg]", fontname="MS Gothic")
        plt.ylabel("仰角 [deg]", fontname="MS Gothic")
        plt.xlim(-90,90)
        plt.ylim(-90,90)
        plt.legend(prop={"family":"MS Gothic"})
        plt.show()
    if mode in ("prism", "All"):
        for i in ("I","W","X","Y"):
            x,y = prismver(i,recommend=recommend)
            plt.scatter(x, y, label=labeldict[i], s=5)
        plt.title("直角プリズム", fontname="MS Gothic")
        plt.xlabel("方位角 [deg]", fontname="MS Gothic")
        plt.ylabel("仰角 [deg]", fontname="MS Gothic")
        plt.xlim(-90,90)
        plt.ylim(-90,90)
        plt.legend(prop={"family":"MS Gothic"})
        plt.show()
    if mode in ("ideal", "All"):
        for i in ("I","W","X","Y"):
            x,y = idealver(i,deg=deg, recommend=recommend)
            plt.scatter(x, y, label=labeldict[i], s=5)
        plt.title("理想状態_%d"%deg, fontname="MS Gothic")
        plt.xlabel("方位角 [deg]", fontname="MS Gothic")
        plt.ylabel("仰角 [deg]", fontname="MS Gothic")
        plt.xlim(-90,90)
        plt.ylim(-90,90)
        plt.legend(prop={"family":"MS Gothic"})
        plt.show()

def All_condition(mode:str, deg = 45, flatisout = True, LP = 40, LPV = 90, recommend = False):
    assert(mode in {"I","W","X","Y"})
    x,y = non(mode, deg=deg, recommend=recommend)
    plt.scatter(x, y, label="屈折なし", s=5)
    x,y = LPver(mode, deg=deg, flatisout=flatisout, LP=LP, recommend=recommend)
    plt.scatter(x, y, label="LP%d"%LP, s=5)
    x,y = LPVver(mode, deg=deg, flatisout=flatisout, LPV=LPV, recommend=recommend)
    plt.scatter(x, y, label="LPV%d"%LPV, s=5)
    x,y = prismver(mode, recommend=recommend)
    plt.scatter(x, y, label="直角プリズム", s=5)
    x,y = idealver(mode, deg=deg, recommend=recommend)
    plt.scatter(x, y, label="理想状態", s=5)
    
    titledict = {"I":"結像光", "W":"両側透過光", "X":"X側透過光", "Y":"Y側透過光"}
    plt.title(titledict[mode], fontname="MS Gothic")
    plt.xlabel("方位角 [deg]", fontname="MS Gothic")
    plt.ylabel("仰角 [deg]", fontname="MS Gothic")
    plt.xlim(-90,90)
    plt.ylim(-90,90)
    plt.legend(prop={"family":"MS Gothic"})
    plt.show()

def compare_deg(mode:str, degs = [45], flatisout = True, LP = 40, LPV = 90, recommend = False):
    assert(mode in {"non", "LP", "LPV", "prism", "ideal"})
    labeldict = {"W": "両側透過光", "X":"X側透過光", "Y":"Y側透過光", "I":"結像光"}
    Mdeg = max(degs)
    mdeg = min(degs)
    for deg in degs:
        for i in ("I","W","X","Y"):
            if mode == "non":
                x,y = non(i,deg=deg, recommend=recommend)
                plt.title("屈折なし", fontname="MS Gothic")
            elif mode == "LP":
                x,y = LPver(i,deg=deg,flatisout=flatisout,LP=LP,recommend=recommend)
                plt.title("LP%d_%d"%(LP,deg), fontname="MS Gothic")
            elif mode == "LPV":
                x,y = LPVver(i,deg=deg,flatisout=flatisout,LPV=LPV,recommend=recommend)
                plt.title("LPV%d_%d"%(LPV,deg), fontname="MS Gothic")
            elif mode == "prism":
                x,y = prismver(i,recommend=recommend)
                plt.title("直角プリズム", fontname="MS Gothic")
            elif mode == "ideal":
                x,y = idealver(i,deg=deg, recommend=recommend)
                plt.title("理想状態_%d"%deg, fontname="MS Gothic")
            else:
                raise ValueError
            nx = [i+deg for i in x]
            plt.scatter(nx, y, label=labeldict[i], s=5)
        plt.xlabel("方位角 [deg]", fontname="MS Gothic")
        plt.ylabel("仰角 [deg]", fontname="MS Gothic")
        plt.xlim(-90+mdeg,90+Mdeg)
        plt.ylim(-90,90)
        plt.legend(prop={"family":"MS Gothic"})
        plt.show()

if __name__ == "__main__":
    # All_mode("All",recommend=True)
    # for i in ("I","W","X","Y"):
    #     unitPlot(i,"non")
    # for i in (30,40):
    #     compare_deg("LP",degs=[30,45,50],LP=i)
    # compare_deg("LPV",degs=[45,70],LPV=130)
    # All_condition("W")
    pass