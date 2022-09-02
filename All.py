from LPintoFlat import LP_into_flat
from LPoutfromFlat import LP_outfrom_flat
from LPVintoFlat import LPV_into_flat
from LPVoutfromFlat import LPV_outfrom_flat

LPs = [15,23,25,30,40]
LPVs = [40,45,60,65,70,75,90,130,140,160]

def non(mode:str,deg = 45, recommend = False):
    assert(mode in {"I","W","X","Y"})
    filenamedict = {"I":"imaging", "W":"transmissive", "X":"Xtransmissive", "Y":"Ytransmissive"}
    filename = filenamedict[mode] + "_non_%d.csv"%deg

    with open(filename, "w", encoding="utf-8") as g:
        print("方位角in0,方位角in1,仰角in,入射角ASKAin,仰角ASKAin,入射角ASKAout,仰角ASKAout,方位角out0,方位角out1,仰角out", file=g)
        for theta_in0 in range(-89,90):
            theta_in1 = theta_in0
            thetaASKAin = theta_in1 - deg
            if not (-90 < thetaASKAin < 90):
                continue
            if recommend:
                if mode == "I":
                    if not (-65 <= thetaASKAin <= -25 or 25 <= thetaASKAin <= 65):
                        continue
                else:
                    if -65 <= thetaASKAin <= -25 or 25 <= thetaASKAin <= 65:
                        continue
            for phi_in in range(-89,90):
                phiASKAin = phi_in
                if recommend:
                    if mode == "I":
                        if not (-65 <= phiASKAin <= -25 or 25 <= phiASKAin <= 65):
                            continue
                    else:
                        if -65 <= phiASKAin <= -25 or 25 <= phiASKAin <= 65:
                            continue
                ASKAdict = {"I":(-thetaASKAin, -phiASKAin), "W":(thetaASKAin, phiASKAin), "X":(phiASKAin, thetaASKAin), "Y":(-phiASKAin, -thetaASKAin)}
                thetaASKAout, phiASKAout = ASKAdict[mode]
                theta_out0 = thetaASKAout - deg
                if not (-90 < theta_out0 < 90):
                    continue
                theta_out1 = theta_out0
                phi_out = phiASKAout
                print("%d,%f,%d,%f,%f,%f,%f,%f,%f,%f"%(theta_in0,theta_in1,phi_in,thetaASKAin,phiASKAin,thetaASKAout,phiASKAout,theta_out0,theta_out1,phi_out), file=g)

def LPver(mode:str, deg = 45, flatisout = True, LP = 40, recommend = False):
    assert(mode in {"I","W","X","Y"})
    filenamedict = {"I":"imaging", "W":"transmissive", "X":"Xtransmissive", "Y":"Ytransmissive"}
    filename = filenamedict[mode] + "_LP%d_%d_flat"%(LP,deg) + ("out" if flatisout else "in") + ("recommend" if recommend else "") + ".csv"

    with open(filename, "w", encoding="utf_8") as g:
        print("方位角in0,方位角in1,仰角in,入射角ASKAin,仰角ASKAin,入射角ASKAout,仰角ASKAout,方位角out0,方位角out1,仰角out", file=g)
        for theta_in0 in range(-89,90):
            theta_in1s = LP_into_flat(theta_in0,LP=LP) if flatisout else LP_outfrom_flat(theta_in0,LP=LP)
            for theta_in1 in theta_in1s:
                thetaASKAin = theta_in1 - deg
                if not (-90 < thetaASKAin < 90):
                    continue
                if recommend:
                    if mode == "I":
                        if not (-65 <= thetaASKAin <= -25 or 25 <= thetaASKAin <= 65):
                            continue
                    else:
                        if -65 <= thetaASKAin <= -25 or 25 <= thetaASKAin <= 65:
                            continue
                for phi_in in range(-89,90):
                    phiASKAin = phi_in
                    if recommend:
                        if mode == "I":
                            if not (-65 <= phiASKAin <= -25 or 25 <= phiASKAin <= 65):
                                continue
                        else:
                            if -65 <= phiASKAin <= -25 or 25 <= phiASKAin <= 65:
                                continue
                    ASKAdict = {"I":(-thetaASKAin, -phiASKAin), "W":(thetaASKAin, phiASKAin), "X":(phiASKAin, thetaASKAin), "Y":(-phiASKAin, -thetaASKAin)}
                    thetaASKAout, phiASKAout = ASKAdict[mode]
                    theta_out0 = thetaASKAout - deg
                    if not (-90 < theta_out0 < 90):
                        continue
                    theta_out1s = LP_outfrom_flat(theta_out0,LP=LP) if flatisout else LP_into_flat(theta_out0,LP=LP)
                    phi_out = phiASKAout
                    for theta_out1 in theta_out1s:
                        print("%d,%f,%d,%f,%f,%f,%f,%f,%f,%f"%(theta_in0,theta_in1,phi_in,thetaASKAin,phiASKAin,thetaASKAout,phiASKAout,theta_out0,theta_out1,phi_out), file=g)

def LPVver(mode:str, deg = 45, flatisout = True, LPV = 90, recommend = False):
    assert(mode in {"I","W","X","Y"})
    filenamedict = {"I":"imaging", "W":"transmissive", "X":"Xtransmissive", "Y":"Ytransmissive"}
    filename = filenamedict[mode] + "_LPV%d_%d_flat"%(LPV,deg) + ("out" if flatisout else "in") + ("recommend" if recommend else "") + ".csv"

    with open(filename, "w", encoding="utf_8") as g:
        print("方位角in0,方位角in1,仰角in,入射角ASKAin,仰角ASKAin,入射角ASKAout,仰角ASKAout,方位角out0,方位角out1,仰角out", file=g)
        for theta_in0 in range(-89,90):
            theta_in1s = LPV_into_flat(theta_in0,LPV=LPV) if flatisout else LPV_outfrom_flat(theta_in0,LPV=LPV)
            for theta_in1 in theta_in1s:
                thetaASKAin = theta_in1 - deg
                if not (-90 < thetaASKAin < 90):
                    continue
                if recommend:
                    if mode == "I":
                        if not (-65 <= thetaASKAin <= -25 or 25 <= thetaASKAin <= 65):
                            continue
                    else:
                        if -65 <= thetaASKAin <= -25 or 25 <= thetaASKAin <= 65:
                            continue
                for phi_in in range(-89,90):
                    phiASKAin = phi_in
                    if recommend:
                        if mode == "I":
                            if not (-65 <= phiASKAin <= -25 or 25 <= phiASKAin <= 65):
                                continue
                        else:
                            if -65 <= phiASKAin <= -25 or 25 <= phiASKAin <= 65:
                                continue
                    ASKAdict = {"I":(-thetaASKAin, -phiASKAin), "W":(thetaASKAin, phiASKAin), "X":(phiASKAin, thetaASKAin), "Y":(-phiASKAin, -thetaASKAin)}
                    thetaASKAout, phiASKAout = ASKAdict[mode]
                    theta_out0 = thetaASKAout - deg
                    if not (-90 < theta_out0 < 90):
                        continue
                    theta_out1s = LPV_outfrom_flat(theta_out0,LPV=LPV) if flatisout else LPV_into_flat(theta_out0,LPV=LPV)
                    phi_out = phiASKAout
                    for theta_out1 in theta_out1s:
                        print("%d,%f,%d,%f,%f,%f,%f,%f,%f,%f"%(theta_in0,theta_in1,phi_in,thetaASKAin,phiASKAin,thetaASKAout,phiASKAout,theta_out0,theta_out1,phi_out), file=g)


def prism(mode:str, recommend = False):
    pass

def ideal(mode:str, recommend = False):
    pass



def All(mode:str, deg = 45, flatisout = True, LP = 40, LPV = 90, recommend = False):
    assert(mode in {"non", "LP", "LPV", "All"})
    if mode in ("non", "All"):
        for i in ("W","X","Y","I"):
            non(i,deg=deg, recommend=recommend)
    if mode in ("LP","All"):
        for i in ("W","X","Y","I"):
            LPver(i,deg=deg,flatisout=flatisout,LP=LP,recommend=recommend)
    if mode in ("LPV","All"):
        for i in ("W","X","Y","I"):
            LPVver(i,deg=deg,flatisout=flatisout,LPV=LPV,recommend=recommend)

def Wside_transmissive(deg = 45, flatisout = True, LP = 40, LPV = 90, recommend = False):
    non("W", deg=deg, recommend=recommend)
    LPver("W", deg=deg, flatisout=flatisout, LP=LP, recommend=recommend)
    LPVver("W", deg=deg, flatisout=flatisout, LPV=LPV, recommend=recommend)

def Xside_transmissive(deg = 45, flatisout = True, LP = 40, LPV = 90, recommend = False):
    non("X", deg=deg, recommend=recommend)
    LPver("X", deg=deg, flatisout=flatisout, LP=LP, recommend=recommend)
    LPVver("X", deg=deg, flatisout=flatisout, LPV=LPV, recommend=recommend)

def Yside_transmissive(deg = 45, flatisout = True, LP = 40, LPV = 90, recommend = False):
    non("Y", deg=deg, recommend=recommend)
    LPver("Y", deg=deg, flatisout=flatisout, LP=LP, recommend=recommend)
    LPVver("Y", deg=deg, flatisout=flatisout, LPV=LPV, recommend=recommend)

def imaging(deg = 45, flatisout = True, LP = 40, LPV = 90, recommend = False):
    non("I", deg=deg, recommend=recommend)
    LPver("I", deg=deg, flatisout=flatisout, LP=LP, recommend=recommend)
    LPVver("I", deg=deg, flatisout=flatisout, LPV=LPV, recommend=recommend)

if __name__ == "__main__":
    All("All")