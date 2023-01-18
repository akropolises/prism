import matplotlib.pyplot as plt

def row_result():
    with open("result.csv", "r", encoding="utf-8-sig") as f:
        data = f.readlines()
    xLP40_0 = []
    yLP40_0 = []
    x_0 = []
    y_0 = []
    xLP40_45 = []
    yLP40_45 = []
    x_45 = []
    y_45 = []
    xLP30_45 = []
    yLP30_45 = []
    xiPad = []
    yiPad = []

    flag_to_x_dict = {1:xLP40_0, 2:x_0, 3:xLP40_45, 4:x_45, 5:xLP30_45, 6:xiPad}
    flag_to_y_dict = {1:yLP40_0, 2:y_0, 3:yLP40_45, 4:y_45, 5:yLP30_45, 6:yiPad}
    label_dict = {1:"LP40ψ30_光源平行", 2:"従来手法_光源平行", 3:"LP40ψ30_光源45°", 4:"従来手法_光源45°", 5:"LP30ψ45_光源45°", 6:"光源"}
    for i in data:
        theta, mean, flag = map(float,i.split(","))
        flag_to_x_dict[flag].append(theta-90)
        flag_to_y_dict[flag].append(mean)
    # BLUE_COLOR_INDEX = 5
    # ORANGE_COLOR_INDEX = 4
    # GREEN_COLOR_INDEX = 6
    # plt.plot(flag_to_x_dict[BLUE_COLOR_INDEX], flag_to_y_dict[BLUE_COLOR_INDEX], label=label_dict[BLUE_COLOR_INDEX], marker = "o", color = "tab:blue")
    # plt.plot(flag_to_x_dict[ORANGE_COLOR_INDEX], flag_to_y_dict[ORANGE_COLOR_INDEX], label=label_dict[ORANGE_COLOR_INDEX], marker = "s", color = "tab:orange")
    # plt.plot(flag_to_x_dict[GREEN_COLOR_INDEX], flag_to_y_dict[GREEN_COLOR_INDEX], label=label_dict[GREEN_COLOR_INDEX], marker = "^", color = "tab:green")
    for i in range(1,7):
        plt.plot(flag_to_x_dict[i], flag_to_y_dict[i], label=label_dict[i], marker = ".")
    plt.xlabel("鑑賞方向(空中像に対する) [deg]", fontname="MS Gothic", fontsize=14)
    plt.ylabel("輝度 [cd/$\mathregular{m^2}$]", fontname="MS Gothic", fontsize=14)
    plt.legend(prop={"family":"MS Gothic"})
    plt.show()

def normalization():
    with open("result.csv", "r", encoding="utf-8-sig") as f:
        data = f.readlines()
    xLP40_0 = []
    yLP40_0 = []
    x_0 = []
    y_0 = []
    xLP40_45 = []
    yLP40_45 = []
    x_45 = []
    y_45 = []
    xLP30_45 = []
    yLP30_45 = []
    iPad = {}
    
    flag_to_x_dict = {1:xLP40_0, 2:x_0, 3:xLP40_45, 4:x_45, 5:xLP30_45}
    flag_to_y_dict = {1:yLP40_0, 2:y_0, 3:yLP40_45, 4:y_45, 5:yLP30_45}
    label_dict = {1:"LP40ψ30_光源平行", 2:"従来手法_光源平行", 3:"LP40ψ30_光源45°", 4:"従来手法_光源45°", 5:"LP30ψ45_光源45°"}
    for i in data:
        theta, mean, flag = map(float,i.split(","))
        if flag == 6:
            iPad[theta-90] = mean
        else:
            flag_to_x_dict[flag].append(theta-90)
            flag_to_y_dict[flag].append(mean)
    for i in range(20,40,5):
        iPad[i] = iPad[-i]

    # BLUE_COLOR_INDEX = 5
    # ORANGE_COLOR_INDEX = 4
    # for i,j in enumerate(flag_to_x_dict[BLUE_COLOR_INDEX]):
    #     # y = iPad[j]
    #     try:
    #         y = iPad[j]
    #     except:
    #         y = (iPad[j+2.5] + iPad[j-2.5])/2
    #     flag_to_y_dict[BLUE_COLOR_INDEX][i] /= y
    #     flag_to_y_dict[BLUE_COLOR_INDEX][i] *= 100
    # plt.plot(flag_to_x_dict[BLUE_COLOR_INDEX], flag_to_y_dict[BLUE_COLOR_INDEX], label=label_dict[BLUE_COLOR_INDEX], marker = "o")
    # for i,j in enumerate(flag_to_x_dict[ORANGE_COLOR_INDEX]):
    #     # y = iPad[j]
    #     try:
    #         y = iPad[j]
    #     except:
    #         y = (iPad[j+2.5] + iPad[j-2.5])/2
    #     flag_to_y_dict[ORANGE_COLOR_INDEX][i] /= y
    #     flag_to_y_dict[ORANGE_COLOR_INDEX][i] *= 100
    # plt.plot(flag_to_x_dict[ORANGE_COLOR_INDEX], flag_to_y_dict[ORANGE_COLOR_INDEX], label=label_dict[ORANGE_COLOR_INDEX], marker = "o")
    for flag in range(1,6):
        for i,j in enumerate(flag_to_x_dict[flag]):
            try:
                y = iPad[j]
            except:
                y = (iPad[j+2.5] + iPad[j-2.5])/2
            flag_to_y_dict[flag][i] /= y
            flag_to_y_dict[flag][i] *= 100
        if flag in (3,4,5):
            flag_to_x_dict[flag] = [i-45 for i in flag_to_x_dict[flag]]
        # plt.plot(flag_to_x_dict[flag], flag_to_y_dict[flag], label=label_dict[flag], marker = ".")
    print(max(flag_to_y_dict[3]))
    print(flag_to_y_dict[3])
    # plt.xlabel("鑑賞方向(RT Plateに対する) [deg]", fontname="MS Gothic", fontsize=14)
    # plt.ylabel("光利用効率 [%]", fontname="MS Gothic", fontsize=14)
    # plt.ylim(0,100)
    # plt.legend(prop={"family":"MS Gothic"})
    # plt.show()

if __name__=="__main__":
    # row_result()
    normalization()