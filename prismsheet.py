from math import sin, asin, pi, degrees, radians
import matplotlib.pyplot as plt
from numpy import NaN
from LPintoFlat import LP_into_flat
from LPoutfromFlat import LP_outfrom_flat

LPs = [15,23,25,30,40]
LPVs = [40,45,60,65,70,75,90,130,140,160]

def plot(on = False, flatisout=True, recommend=False):
    for LP in LPs:
        x = []
        y = []
        ranges = [i/10 for i in range(-899,900)]
        for i in ranges:
            try:
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

# plot(on=True,flatisout=True)
# plot(on=True,flatisout=False)
# plot(on=False,flatisout=True)
# plot(on=False,flatisout=False)
plot(on=True,flatisout=True,recommend=True)
plot(on=True,flatisout=False,recommend=True)
# plot(on=False,flatisout=True,recommend=True)
# plot(on=False,flatisout=False,recommend=True)




# def LP_ASKA3D_45deg_flatisout():
#     for LP in LPs:
#         x = []
#         y = []
#         for i in range(-89,90):
#             try:
#                 tmp = LP_into_flat(i,LP=LP)
#                 out = []
#                 for j in tmp:
#                     # if -65 <= j-45 <= -25 or 25 <= j-45 <= 65:
#                     out += LP_outfrom_flat(-j,LP=LP)
#             except:
#                 out = []
#             for j in out:
#                 x.append(i)
#                 y.append(j)
#         plt.scatter(x,y,label="LP=%d°"%LP,s = 5)
#     plt.title("プリズムシート(LP)ASKA3Dに対し45°に置いた場合(外側平面)", fontname="MS Gothic")
#     plt.xlabel("プリズムシート入射角 [deg]", fontname="MS Gothic")
#     plt.ylabel("プリズムシート出射角 [deg]", fontname="MS Gothic")
#     plt.legend()
#     plt.show()

# def LP_ASKA3D_45deg_flatisin():
#     for LP in LPs:
#         x = []
#         y = []
#         for i in range(-89,90):
#             try:
#                 tmp = LP_outfrom_flat(i,LP=LP)
#                 out = []
#                 for j in tmp:
#                     # if -65 <= j-45 <= -25 or 25 <= j-45 <= 65:
#                     out += LP_into_flat(-j,LP=LP)
#             except:
#                 out = []
#             for j in out:
#                 x.append(i)
#                 y.append(j)
#         plt.scatter(x,y,label="LP=%d°"%LP,s = 5)
#     plt.title("プリズムシート(LP)ASKA3Dに対し45°に置いた場合(内側平面)", fontname="MS Gothic")
#     plt.xlabel("プリズムシート入射角 [deg]", fontname="MS Gothic")
#     plt.ylabel("プリズムシート出射角 [deg]", fontname="MS Gothic")
#     plt.legend()
#     plt.show()

# def LPonASKA3D_flatisout():
#     for LP in LPs:
#         x = []
#         y = []
#         for i in range(-89,90):
#             try:
#                 tmp = LP_into_flat(i,LP=LP)
#                 out = []
#                 for j in tmp:
#                     # if -65 <= j <= -25 or 25 <= j <= 65:
#                     out += LP_outfrom_flat(-j,LP=LP)
#             except:
#                 out = []
#             for j in out:
#                 x.append(i)
#                 y.append(j)
#         plt.scatter(x,y,label="LP=%d°"%LP,s = 5)
#     plt.title("プリズムシート(LP)ASKA3Dに貼り付けた場合(外側平面)", fontname="MS Gothic")
#     plt.xlabel("プリズムシート入射角 [deg]", fontname="MS Gothic")
#     plt.ylabel("プリズムシート出射角 [deg]", fontname="MS Gothic")
#     plt.legend()
#     plt.show()

# def LPonASKA3D_flatisin():
#     for LP in LPs:
#         x = []
#         y = []
#         for i in range(-89,90):
#             try:
#                 tmp = LP_outfrom_flat(i,LP=LP)
#                 out = []
#                 for j in tmp:
#                     # if -65 <= j <= -25 or 25 <= j <= 65:
#                     out += LP_into_flat(-j,LP=LP)
#             except:
#                 out = []
#             for j in out:
#                 x.append(i)
#                 y.append(j)
#         plt.scatter(x,y,label="LP=%d°"%LP,s = 5)
#     plt.title("プリズムシート(LP)ASKA3Dに貼り付けた場合(内側平面)", fontname="MS Gothic")
#     plt.xlabel("プリズムシート入射角 [deg]", fontname="MS Gothic")
#     plt.ylabel("プリズムシート出射角 [deg]", fontname="MS Gothic")
#     plt.legend()
#     plt.show()

# LP_ASKA3D_45deg_flatisout()
# LP_ASKA3D_45deg_flatisin()
# LPonASKA3D_flatisout()
# LPonASKA3D_flatisin()