from math import sin, asin, pi, degrees, radians
from turtle import title
import matplotlib.pyplot as plt
from numpy import NaN
from LPintoFlat import LP_into_flat
from LPoutfromFlat import LP_outfrom_flat
from LPVintoFlat import LPV_into_flat
from LPVoutfromFlat import LPV_outfrom_flat

LPs = [15,23,25,30,40]
LPVs = [40,45,60,65,70,75,90,130,140,160]

def plot(arg, title):
    for filename,labelstr in arg:
        with open(filename, "r", encoding="utf-8") as f:
            l = f.readline()
            l = f.readlines()
            theta = []
            phi = []
            for i in l:
                i = list(map(float,i.split(",")))
                theta.append(i[-2])
                phi.append(i[-1])
            plt.scatter(theta, phi, label = labelstr, s=5)
    plt.title(title, fontname="MS Gothic")
    plt.xlabel("方位角 [deg]", fontname="MS Gothic")
    plt.ylabel("仰角 [deg]", fontname="MS Gothic")
    plt.xlim(-90,90)
    plt.ylim(-90,90)
    plt.legend()
    plt.show()

# arg = [("imaging_non_45.csv","結像光")] 
# arg = [("imaging_non_45.csv","imaging light"), ("transmissive_non_45.csv","both side"), 
#     ("Xtransmissive_non_45.csv","X side"), ("Ytransmissive_non_45.csv","Y side")]
# title = "屈折無し"
# arg = [("imaging_LP40_45_1.csv","imaging light"), ("transmissive_LP40_45_1.csv","both side"), 
#     ("Xtransmissive_LP40_45_1.csv","X side"), ("Ytransmissive_LP40_45_1.csv","Y side")]
# title = "LP40"
# arg = [("imaging_LPV90_45_1.csv","imaging light"), ("transmissive_LPV90_45_1.csv","both side"), 
#     ("Xtransmissive_LPV90_45_1.csv","X side"), ("Ytransmissive_LPV90_45_1.csv","Y side")]
# title = "LPV90"
# arg = [("imaging_LPV130_45_1.csv","imaging light"), ("transmissive_LPV130_45_1.csv","both side"), 
#     ("Xtransmissive_LPV130_45_1.csv","X side"), ("Ytransmissive_LPV130_45_1.csv","Y side")]
# title = "LPV130"
arg = [("imaging_LPV75_45_1.csv","imaging light"), ("transmissive_LPV75_45_1.csv","both side"), 
    ("Xtransmissive_LPV75_45_1.csv","X side"), ("Ytransmissive_LPV75_45_1.csv","Y side")]
title = "LPV75"

if __name__ == "__main__":
    plot(arg,title)