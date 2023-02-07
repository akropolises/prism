from math import sin, asin, pi, degrees, radians
import matplotlib.pyplot as plt

n = 1.49 #PMMA

def LP_into_flat(incidentAngle_degree,LP=40):
    """ 
    LPタイプのプリズムシートに平面側から光を入射させプリズム側から出射させた時の角度

    Args:
        incidentAngle_degree : int 
            プリズムシート入射角(度数法)\n
            プリズムシートに垂直を0°とし、左を負、右を正とする
        LP : int
            LPタイプのプリズムシートの角度\n
            日本特殊光学樹脂製の存在する角度：[15,23,25,30,40]
    
    Returns:
        float : プリズムシート出射角(度数法)
            プリズムシートに垂直を0°とし、右へ向かうのを負、左へ向かうのを正とする。
    """
    assert(-90<incidentAngle_degree<90)
    in1 = radians(incidentAngle_degree)
    LP = radians(LP)
    #1*sin(in1) = n*sin(out1)
    out1 = asin(sin(in1)/n)
    ret = []
    if out1 > -(pi/2 - LP): #左斜面
        in2 = out1 - LP
        try:
            out2 = asin(n*sin(in2))
            out = out2 + LP
            ret.append(degrees(out))
        except:
            pass
    # if out1 < 0: # 壁
    #     in2 = pi/2 + out1 #out1<0に注意
    #     try:
    #         out2 = asin(n*sin(in2))
    #         out = out2 - pi/2
    #         ret.append(degrees(out))
    #     except:
    #         out1 = -out1
    #         if out1 > -(pi/2 - LP): #左斜面
    #             in2 = out1 - LP
    #             try:
    #                 out2 = asin(n*sin(in2))
    #                 out = out2 + LP
    #                 ret.append(degrees(out))
    #             except:
    #                 pass
    return ret

def plot():
    LPs = [15,23,25,30,40]
    for LP in LPs:
        x = []
        y = []
        for i in range(-89,90):
            j = LP_into_flat(i,LP=LP)
            if j:
                x.append(i)
                y.append(j[0])
        # plt.scatter(x,y,label="LP%d"%LP,s = 5)
        plt.plot(x,y,label="%d°"%LP)
    # plt.title("プリズムシートLP平面から入射", fontname="MS Gothic")
    plt.xlabel("プリズムシート入射角 [deg]", fontname="MS Gothic", fontsize = 14)
    plt.ylabel("プリズムシート出射角 [deg]", fontname="MS Gothic", fontsize = 14)
    plt.xlim(-90,90)
    plt.ylim(-90,90)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot()