from numpy import NaN
from LPintoFlat import LP_into_flat
from LPoutfromFlat import LP_outfrom_flat
from LPVintoFlat import LPV_into_flat
from LPVoutfromFlat import LPV_outfrom_flat

LPs = [15,23,25,30,40]
LPVs = [40,45,60,65,70,75,90,130,140,160]

def non_Xtransmissive(deg = 45):
    with open("Xtransmissive_non_%d.csv"%deg, "w", encoding="utf-8") as g:
        print("方位角in0,方位角in1,仰角in,入射角ASKAin,仰角ASKAin,入射角ASKAout,仰角ASKAout,方位角out0,方位角out1,仰角out", file=g)
        for theta_in0 in range(-89,90):
            theta_in1 = theta_in0
            thetaASKAin = theta_in1 - deg
            if not (-90 < thetaASKAin < 90):
                continue
            for phi_in in range(-89,90):
                phiASKAin = phi_in 
                thetaASKAout, phiASKAout = phiASKAin, thetaASKAin
                theta_out0 = thetaASKAout - deg
                if not (-90 < theta_out0 < 90):
                    continue
                theta_out1 = theta_out0
                phi_out = phiASKAout
                print("%d,%f,%d,%f,%f,%f,%f,%f,%f,%f"%(theta_in0,theta_in1,phi_in,thetaASKAin,phiASKAin,thetaASKAout,phiASKAout,theta_out0,theta_out1,phi_out), file=g)

def LP_Xtransmissive(deg = 45, flatisout = True, LP = 40):
    with open("Xtransmissive_LP%d_%d_%d.csv"%(LP,deg,flatisout), "w", encoding="utf_8") as g:
        print("方位角in0,方位角in1,仰角in,入射角ASKAin,仰角ASKAin,入射角ASKAout,仰角ASKAout,方位角out0,方位角out1,仰角out", file=g)
        for theta_in0 in range(-89,90):
            theta_in1s = LP_into_flat(theta_in0,LP=LP) if flatisout else LP_outfrom_flat(theta_in0,LP=LP)
            for theta_in1 in theta_in1s:
                thetaASKAin = theta_in1 - deg
                if not (-90 < thetaASKAin < 90):
                    continue
                for phi_in in range(-89,90):
                    phiASKAin = phi_in 
                    thetaASKAout, phiASKAout = phiASKAin, thetaASKAin
                    theta_out0 = thetaASKAout - deg
                    if not (-90 < theta_out0 < 90):
                        continue
                    theta_out1s = LP_outfrom_flat(theta_out0,LP=LP) if flatisout else LP_into_flat(theta_out0,LP=LP)
                    phi_out = phiASKAout
                    for theta_out1 in theta_out1s:
                        print("%d,%f,%d,%f,%f,%f,%f,%f,%f,%f"%(theta_in0,theta_in1,phi_in,thetaASKAin,phiASKAin,thetaASKAout,phiASKAout,theta_out0,theta_out1,phi_out), file=g)

def LPV_Xtransmissive(deg = 45, flatisout = True, LPV = 90):
    with open("Xtransmissive_LPV%d_%d_%d.csv"%(LPV,deg,flatisout), "w", encoding="utf_8") as g:
        print("方位角in0,方位角in1,仰角in,入射角ASKAin,仰角ASKAin,入射角ASKAout,仰角ASKAout,方位角out0,方位角out1,仰角out", file=g)
        for theta_in0 in range(-89,90):
            theta_in1s = LPV_into_flat(theta_in0,LPV=LPV) if flatisout else LPV_outfrom_flat(theta_in0,LPV=LPV)
            for theta_in1 in theta_in1s:
                thetaASKAin = theta_in1 - deg
                if not (-90 < thetaASKAin < 90):
                    continue
                for phi_in in range(-89,90):
                    phiASKAin = phi_in 
                    thetaASKAout, phiASKAout = phiASKAin, thetaASKAin
                    theta_out0 = thetaASKAout - deg
                    if not (-90 < theta_out0 < 90):
                        continue
                    theta_out1s = LPV_outfrom_flat(theta_out0,LPV=LPV) if flatisout else LPV_into_flat(theta_out0,LPV=LPV)
                    phi_out = phiASKAout
                    for theta_out1 in theta_out1s:
                        print("%d,%f,%d,%f,%f,%f,%f,%f,%f,%f"%(theta_in0,theta_in1,phi_in,thetaASKAin,phiASKAin,thetaASKAout,phiASKAout,theta_out0,theta_out1,phi_out), file=g)


def main(deg = 45, flatisout = True, LP = 40, LPV = 90):
    non_Xtransmissive(deg=deg)
    LP_Xtransmissive(deg=deg,flatisout=flatisout,LP=LP)
    LPV_Xtransmissive(deg=deg,flatisout=flatisout,LPV=LPV)

if __name__ == "__main__":
    main()