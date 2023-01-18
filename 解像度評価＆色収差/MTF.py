import cv2
from collections import defaultdict
from math import sin, cos, radians
from matplotlib import pyplot as plt
import numpy as np

def ESF(mode:str):
    image_file_name = "./MTF" + mode + ".png"
    I = cv2.imread(image_file_name, cv2.IMREAD_GRAYSCALE)
    h,w = I.shape
    # cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    # cv2.imshow("img", I)
    # cv2.waitKey(0)
    d = defaultdict(list)
    c = cos(radians(3))
    s = sin(radians(3))
    for i in range(h-1,-1,-1):
        for j in range(w):
            d[int((h-1-i)*s+j*c)].append(I[i][j])
    M = max(d.keys())
    dp = [0]*(M+1)
    for i in range(M+1):
        dp[i] = sum(d[i])/len(d[i])
    return dp
    plt.plot(dp)
    plt.xlim(0,M)
    # plt.ylim(0,255)
    plt.xlabel("position [pixels]", fontsize = 14)
    plt.ylabel("gray scale level", fontsize = 14)
    plt.show()
    txt_file_name = "ESF" + mode + ".txt"
    with open(txt_file_name, mode="w", encoding="utf-8") as f:
        print(dp,file=f)

def LSF(ESF:list):
    ret = []
    for i in range(len(ESF)-1):
        ret.append(ESF[i+1] - ESF[i])
    # plt.plot(ret)
    # plt.xlabel("position [pixels]", fontsize = 14)
    # plt.ylabel("gray scale level", fontsize = 14)
    # plt.show()
    return ret

def MTF():
    LSFc = LSF(ESF("conventional"))[:2600]
    Nc = len(LSFc)
    hc = 1400/109 # conventional
    freqc = np.fft.fftfreq(Nc, 1/hc)
    lsf_fftc = abs(np.fft.fft(LSFc))
    lsf_fftc /= lsf_fftc[0]
    plt.plot(freqc[:Nc//2], lsf_fftc[:Nc//2], label = "従来手法")
    LSFp = LSF(ESF("proposed"))
    Np = len(LSFp)
    hp = 1760/109 # proposed
    freqp = np.fft.fftfreq(Np, 1/hp)
    lsf_fftp = abs(np.fft.fft(LSFp))
    lsf_fftp /= lsf_fftp[0]
    plt.plot(freqp[:Np//2], lsf_fftp[:Np//2], label = "提案手法")
    plt.xlim(0,3)
    plt.xlabel("lp/mm", fontsize = 14)
    plt.ylabel("MTF", fontsize = 14)
    plt.legend(prop={"family":"MS Gothic"})
    plt.show()

if __name__ == "__main__":
    # ESF("conventional")
    # ESF("proposed")
    # LSF(ESF("conventional"))
    # LSF(ESF("proposed"))
    MTF()