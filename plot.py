from math import acos,degrees,radians,tan
import matplotlib.pyplot as plt
from LPintoFlat import LP_into_flat
from LPoutfromFlat import LP_outfrom_flat
from LPVintoFlat import LPV_into_flat
from LPVoutfromFlat import LPV_outfrom_flat
# from right_angle_prism import prism
from ideal import idealRefractionIn, idealRefractionOut

LPs = [15,23,25,30,40]
LPVs = [40,45,60,65,70,75,90,130,140,160]

class CoordinateTransformation:

    def theta_in0_to_theta_in1(theta_in0, item:str, LP=40, LPV=90, flatisout = True):
        d = {"non":theta_in0, "ideal":idealRefractionIn(theta_in0)}
        d["LP"] = LP_into_flat(theta_in0,LP=LP) if flatisout else LP_outfrom_flat(theta_in0,LP=LP)
        return d[item]
    
    def theta_in1_to_theta_AIP_in(theta_in1, item:str, deg):
        if item == "prism":
            pass
        else:
            return theta_in1 - deg
    
    def phi_in_to_phi_AIP_in(phi_in, item:str):
        if item == "ideal":
            return idealRefractionIn(phi_in)
        else:
            return phi_in
    
    def theta_AIP_out_to_theta_out0(theta_AIP_out, item:str, deg):
        if item == "prism":
            pass
        else:
            return theta_AIP_out - deg

    def phi_AIP_out_to_phi_out(phi_AIP_out, item:str):
        if item == "ideal":
            return idealRefractionOut(phi_AIP_out)
        else:
            return phi_AIP_out
    
    def theta_out0_to_theta_out1(theta_out0, item:str, LP=40, LPV=90, flatisout = True):
        d = {"non":theta_out0, "ideal":idealRefractionOut(theta_out0)}
        d["LP"] = LP_outfrom_flat(theta_out0,LP=LP) if flatisout else LP_into_flat(theta_out0,LP=LP)
        return d[item]

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
                phi_out = phiASKAout
                if not (-90 < theta_out0 < 90):
                    if mode != "I":
                        theta.append(theta_out0 + deg)
                        phi.append(phi_out)
                else:
                    theta_out1s = LPV_outfrom_flat(theta_out0,LPV=LPV) if flatisout else LPV_into_flat(theta_out0,LPV=LPV)
                    for theta_out1 in theta_out1s:
                        theta.append(theta_out1 + deg)
                        phi.append(phi_out)
    return theta, phi


def make_emission_angle_list(item:str, light_type:str,  deg = 45, LP = 40, LPV = 90, recommend = False, flatisout = True):
    assert(item in {"non", "LP", "LPV", "prism", "ideal"})
    assert(light_type in {"I","W","X","Y"})

    if item == "prism":
        exit(print("execute right_angle_prism.py directly"))
    elif item == "LPV":
        print("exception")
        return LPVver(light_type,deg=deg,flatisout=flatisout,LPV=LPV,recommend=recommend)

    theta = []
    phi = []

    for theta_in0 in range(-89,90):
        theta_in1 = CoordinateTransformation.theta_in0_to_theta_in1(theta_in0,item,LP,LPV,flatisout)
        if theta_in1 is None:
            continue
        theta_AIP_in = CoordinateTransformation.theta_in1_to_theta_AIP_in(theta_in1,item,deg)
        if not (-90 < theta_AIP_in < 90):
            continue
        for phi_in in range(-89,90):
            phi_AIP_in = CoordinateTransformation.phi_in_to_phi_AIP_in(phi_in,item)
            if not (-90 < phi_AIP_in < 90):
                continue
            if recommend:
                thetaR = radians(theta_AIP_in)
                phiR = radians(phi_AIP_in)
                psi = 90 - degrees(acos(1/(tan(thetaR)**2 + tan(phiR)**2 + 1)**(1/2)))
                if light_type == "I":
                    if not (25 <= psi <= 65):
                        continue
                else:
                    if 25 <= psi <= 65:
                        continue
            AIP_dict = {"I":(-theta_AIP_in, -phi_AIP_in), "W":(theta_AIP_in, phi_AIP_in), "X":(phi_AIP_in, theta_AIP_in), "Y":(-phi_AIP_in, -theta_AIP_in)}
            theta_AIP_out, phi_AIP_out = AIP_dict[light_type]
            theta_out0 = CoordinateTransformation.theta_AIP_out_to_theta_out0(theta_AIP_out, item, deg)
            phi_out = CoordinateTransformation.phi_AIP_out_to_phi_out(phi_AIP_out, item)
            if not (-90 < theta_out0 < 90):
                if light_type != "I":
                    theta.append(theta_out0 + deg)
                    phi.append(phi_out)
            else:
                theta_out1 = CoordinateTransformation.theta_out0_to_theta_out1(theta_out0,item,LP,LPV,flatisout)
                if theta_out1 is None:
                    continue
                theta.append(theta_out1 + deg)
                phi.append(phi_out)
    return theta, phi
            
class Plot:

    def common(self,deg):
        plt.xlabel("方位角 [deg]", fontname="MS Gothic")
        plt.ylabel("仰角 [deg]", fontname="MS Gothic")
        plt.xlim(-90+deg,90+deg)
        plt.ylim(-90,90)
        plt.legend(prop={"family":"MS Gothic"})
        plt.show()

    def plot_unit(self, light_type:str, item:str, deg = 45, flatisout = True, LP = 40, LPV = 90, recommend = False):
        label_dict = {"W": "両側透過光", "X":"X側透過光", "Y":"Y側透過光", "I":"結像光"}
        color_dict = {"I":"tab:blue", "W":"tab:orange", "X":"tab:green", "Y":"tab:red"}
        title_dict = {"non":"屈折なし", "LP":"LP%d"%LP, "LPV":"LPV%d"%LPV, "prism":"直角プリズム", "ideal":"理想状態"}
        x,y = make_emission_angle_list(item, light_type, deg, LP, LPV, recommend, flatisout)
        plt.scatter(x, y, label=label_dict[light_type], s=5, c=color_dict[light_type])
        plt.title(title_dict[item], fontname="MS Gothic")
        self.common(deg)

    def plot_all_light_type(self, item:str, deg = 45, flatisout = True, LP = 40, LPV = 90, recommend = False):
        assert(item in {"non", "LP", "LPV", "prism", "ideal"})
        labeldict = {"W": "両側透過光", "X":"X側透過光", "Y":"Y側透過光", "I":"結像光"}
        title_dict = {"non":"屈折なし", "LP":"LP%d_30"%LP, "LPV":"LPV%d"%LPV, "prism":"直角プリズム", "ideal":"理想状態"}
        
        for light_type in ("I","W","X","Y"):
            x,y = make_emission_angle_list(item, light_type, deg, LP, LPV, recommend, flatisout)
            plt.scatter(x, y, label=labeldict[light_type], s=5)
        plt.title(title_dict[item], fontname="MS Gothic")
        self.common(deg)

    def plot_all_item(self, light_type:str, deg = 45, flatisout = True, LP = 40, LPV = 90, recommend = False):
        assert(light_type in {"I","W","X","Y"})
        label_dict = {"non":"屈折なし", "LP":"LP%d"%LP, "LPV":"LPV%d"%LPV, "prism":"直角プリズム", "ideal":"理想状態"}
        titledict = {"I":"結像光", "W":"両側透過光", "X":"X側透過光", "Y":"Y側透過光"}

        for item in ("non", "LP", "LPV", "prism", "ideal"):
            x,y = make_emission_angle_list(item, light_type, deg, LP, LPV, recommend, flatisout)
            plt.scatter(x, y, label=label_dict[item], s=5)    
        plt.title(titledict[light_type], fontname="MS Gothic")
        self.common(deg)

    def compare_deg(self, item:str, degs = [45], flatisout = True, LP = 40, LPV = 90, recommend = False):
        assert(item in {"non", "LP", "LPV", "prism", "ideal"})
        labeldict = {"W": "両側透過光", "X":"X側透過光", "Y":"Y側透過光", "I":"結像光"}
        title_dict = {"non":"屈折なし", "LP":"LP%d"%LP, "LPV":"LPV%d"%LPV, "prism":"直角プリズム", "ideal":"理想状態"}
        Mdeg = max(degs)
        mdeg = min(degs)
        
        for deg in degs:
            for light_type in ("I","W","X","Y"):
                x,y = make_emission_angle_list(item, light_type, deg, LP, LPV, recommend, flatisout)
                plt.scatter(x, y, label=labeldict[light_type], s=5)
            plt.title(title_dict[item], fontname="MS Gothic")
            # self.common(deg)はxlimを変えるため使わない
            plt.xlabel("方位角 [deg]", fontname="MS Gothic")
            plt.ylabel("仰角 [deg]", fontname="MS Gothic")
            plt.xlim(-90+mdeg,90+Mdeg)
            plt.ylim(-90,90)
            plt.legend(prop={"family":"MS Gothic"})
            plt.show()

if __name__ == "__main__":
    fig = Plot()
    fig.plot_all_light_type("LPV", LPV=75)
    # for i in ("I","W","X","Y"):
    #     fig.plot_unit(i,"non")
    # for i in (30,40):
    #     fig.compare_deg("LP",degs=[30,45,50],LP=i)
    # fig.compare_deg("LPV",degs=[45,70],LPV=130)
    # fig.plot_all_item("W")
    pass