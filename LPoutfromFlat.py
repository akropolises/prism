from math import sin, asin, pi, degrees, radians
import matplotlib.pyplot as plt

n = 1.49 #PMMA

def LP_outfrom_flat(incidentAngle_degree,LP=40):
    """ 
    LPタイプのプリズムシートにプリズム側から光を入射させ平面側から出射させた時の角度

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
    in0 = radians(incidentAngle_degree)
    LP = radians(LP)
    ret = []
    if in0 < pi/2 - LP: #斜面
        in1 = in0 + LP
        out1 = asin(sin(in1)/n)
        if out1 > -(pi/2 - LP): # 平面
            in2 = out1 - LP
            try:
                out = asin(n*sin(in2))
                ret.append(degrees(out))
            except:
                pass
        # if out1 < LP: # 壁
        #     in2 = LP-out1
        #     try:
        #         out = asin(n*sin(in2))
        #         ret.append(degrees(out))
        #     except:
        #         pass
    # if in0 > 0: # 壁
    #     in1 = pi/2 - in0
    #     out1 = asin(sin(in1)/n)
    #     in2 = pi/2 - out1
    #     try:
    #         out = asin(n*sin(in2))
    #         ret.append(degrees(out))
    #     except:
    #         pass
    return ret

def plot():
    LPs = [15,23,25,30,40]
    for LP in LPs:
        x = []
        y = []
        for i in range(-89,90):
            j = LP_outfrom_flat(i,LP=LP)
            x.append(i)
            y.append(j)
        plt.scatter(x,y,label="LP%d"%LP,s = 5)
    plt.title("プリズムシートLP平面から出射", fontname="MS Gothic")
    plt.xlabel("プリズムシート入射角 [deg]", fontname="MS Gothic")
    plt.ylabel("プリズムシート出射角 [deg]", fontname="MS Gothic")
    plt.xlim(-90,90)
    plt.ylim(-90,90)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot()