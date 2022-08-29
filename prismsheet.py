from math import sin, asin, pi, degrees, radians
import matplotlib.pyplot as plt
from numpy import NaN
from LPintoFlat import LP_into_flat
from LPoutfromFlat import LP_outfrom_flat
from LPVintoFlat import LPV_into_flat
from LPVoutfromFlat import LPV_outfrom_flat

LPs = [15,23,25,30,40]
LPVs = [40,45,60,65,70,75,90,130,140,160]

def plotLP(on = False, flatisout=True, recommend=False):
    for LP in LPs:
        x = []
        y = []
        ranges = [i/10 for i in range(-899,900)]
        for i in ranges:
            try:
                if on:
                    tmp = LP_into_flat(i-45,LP=LP) if flatisout else LP_outfrom_flat(i-45,LP=LP)
                else:
                    tmp = LP_into_flat(i,LP=LP) if flatisout else LP_outfrom_flat(i,LP=LP)
                out = []
                for j in tmp:
                    if recommend:
                        if on:
                            if -65 <= j <= -25 or 25 <= j <= 65:
                                out += LP_outfrom_flat(-j,LP=LP) if flatisout else LP_into_flat(-j,LP=LP)
                        else:
                            if j > -45 and (-65 <= j-45 <= -25 or 25 <= j-45 <= 65):
                                out += LP_outfrom_flat(-j,LP=LP) if flatisout else LP_into_flat(-j,LP=LP)
                    else:
                        if on:
                            out += LP_outfrom_flat(-j,LP=LP) if flatisout else LP_into_flat(-j,LP=LP)
                        else:
                            if j > -45:
                                out += LP_outfrom_flat(-j,LP=LP) if flatisout else LP_into_flat(-j,LP=LP)
            except:
                out = []
            for j in out:
                x.append(i)
                if on:
                    y.append(j-45)
                else:
                    y.append(j)
        plt.scatter(x,y,label="LP=%d°"%LP,s = 5)
    titleOn = "プリズムシート(LP)ASKA3Dに貼り付けた場合" if on else "プリズムシート(LP)ASKA3Dに対し45°に置いた場合"
    titleOut = "(外側平面)" if flatisout else "(内側平面)"
    titleRec = " 推奨入射角のみ採用" if recommend else ""
    plt.title(titleOn+titleOut+titleRec, fontname="MS Gothic")
    plt.xlabel("プリズムシート入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("プリズムシート出射角 [deg]", fontname="MS Gothic")
    plt.xlim(-90,90)
    plt.ylim(-90,90)
    plt.legend()
    plt.show()

# plotLP(on=True,flatisout=True)
# plotLP(on=True,flatisout=False)
# plotLP(on=False,flatisout=True)
# plotLP(on=False,flatisout=False)
# plotLP(on=True,flatisout=True,recommend=True)
# plotLP(on=True,flatisout=False,recommend=True)
# plotLP(on=False,flatisout=True,recommend=True)
# plotLP(on=False,flatisout=False,recommend=True)

def plotLPV(on = False, flatisout=True, recommend=False, deg = 45):
    for LPV in LPVs:
        x = []
        y = []
        ranges = [i/10 for i in range(-899,900)]
        for i in ranges:
            try:
                if on:
                    tmp = LPV_into_flat(i-45,LPV=LPV) if flatisout else LPV_outfrom_flat(i-45,LPV=LPV)
                else:
                    tmp = LPV_into_flat(i,LPV=LPV) if flatisout else LPV_outfrom_flat(i,LPV=LPV)
                out = []
                for j in tmp:
                    if recommend:
                        if on:
                            if -65 <= j <= -25 or 25 <= j <= 65:
                                out += LPV_outfrom_flat(-j,LPV=LPV) if flatisout else LPV_into_flat(-j,LPV=LPV)
                        else:
                            if j > -45 and (-65 <= j-45 <= -25 or 25 <= j-45 <= 65):
                                out += LPV_outfrom_flat(-j,LPV=LPV) if flatisout else LPV_into_flat(-j,LPV=LPV)
                    else:
                        if on:
                            out += LPV_outfrom_flat(-j,LPV=LPV) if flatisout else LPV_into_flat(-j,LPV=LPV)
                        else:
                            if j > -45:
                                out += LPV_outfrom_flat(-j,LPV=LPV) if flatisout else LPV_into_flat(-j,LPV=LPV)
            except:
                out = []
            for j in out:
                x.append(i)
                if on:
                    y.append(j-45)
                else:
                    y.append(j)
        plt.scatter(x,y,label="LPV=%d°"%LPV,s = 5)
    titleOn = "プリズムシート(LPV)ASKA3Dに貼り付けた場合" if on else "プリズムシート(LPV)ASKA3Dに対し45°に置いた場合"
    titleOut = "(外側平面)" if flatisout else "(内側平面)"
    titleRec = " 推奨入射角のみ採用" if recommend else ""
    plt.title(titleOn+titleOut+titleRec, fontname="MS Gothic")
    plt.xlabel("プリズムシート入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("プリズムシート出射角 [deg]", fontname="MS Gothic")
    plt.xlim(-90,90)
    plt.ylim(-90,90)
    plt.legend()
    plt.show()

plotLPV(on=True,flatisout=True)
plotLPV(on=True,flatisout=False)
plotLPV(on=False,flatisout=True)
plotLPV(on=False,flatisout=False)
# plotLPV(on=True,flatisout=True,recommend=True)
# plotLPV(on=True,flatisout=False,recommend=True)
# plotLPV(on=False,flatisout=True,recommend=True)
# plotLPV(on=False,flatisout=False,recommend=True)