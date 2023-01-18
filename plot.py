from enum import Enum, auto
from math import acos,degrees,radians,tan
import matplotlib.pyplot as plt
from LPintoFlat import LP_into_flat
from LPoutfromFlat import LP_outfrom_flat
from LPVintoFlat import LPV_into_flat
from LPVoutfromFlat import LPV_outfrom_flat
from right_angle_prism import plot_viewangle
from ideal import idealRefractionIn, idealRefractionOut

LPs = [15,23,25,30,40]
LPVs = [40,45,60,65,70,75,90,130,140,160]

class Item(Enum):
    non = auto()
    LP = auto()
    LPV = auto()
    prism = auto()
    ideal = auto()

class LightType(Enum):
    I = "結像光"
    W = "両側透過光"
    X = "X側透過光"
    Y = "Y側透過光"

class Transposer:

    @staticmethod
    def __theta_in0_to_theta_in1(theta_in0, item:Item, LP=40, LPV=90, flatisout = True):
        if item == Item.LP:
            return LP_into_flat(theta_in0,LP=LP) if flatisout else LP_outfrom_flat(theta_in0,LP=LP)
        if item == Item.LPV:
            return LPV_into_flat(theta_in0,LPV=LPV) if flatisout else LPV_outfrom_flat(theta_in0,LPV=LPV)
        d = {Item.non:theta_in0, Item.ideal:idealRefractionIn(theta_in0)}
        return [d[item]]
    
    @staticmethod
    def __theta_in1_to_theta_AIP_in(theta_in1, item:Item, deg):
        if item == Item.prism:
            pass
        else:
            return theta_in1 - deg
    
    @staticmethod
    def __phi_in_to_phi_AIP_in(phi_in, item:Item):
        if item == Item.ideal:
            return idealRefractionIn(phi_in)
        else:
            return phi_in
    
    @staticmethod
    def __theta_AIP_out_to_theta_out0(theta_AIP_out, item:Item, deg):
        if item == Item.prism:
            pass
        else:
            return theta_AIP_out - deg

    @staticmethod
    def __phi_AIP_out_to_phi_out(phi_AIP_out, item:Item):
        if item == Item.ideal:
            return idealRefractionOut(phi_AIP_out)
        else:
            return phi_AIP_out
    
    @staticmethod
    def __theta_out0_to_theta_out1(theta_out0, item:Item, LP=40, LPV=90, flatisout = True):
        if item == Item.LP:
            return LP_outfrom_flat(theta_out0,LP=LP) if flatisout else LP_into_flat(theta_out0,LP=LP)
        if item == Item.LPV:
            return LPV_outfrom_flat(theta_out0,LPV=LPV) if flatisout else LPV_into_flat(theta_out0,LPV=LPV)
        d = {Item.non:theta_out0, Item.ideal:idealRefractionOut(theta_out0)}
        return [d[item]]

    @staticmethod
    def make_emission_angle_list(item:Item, light_type:LightType,  deg = 45, LP = 40, LPV = 90, recommend = False, flatisout = True):
        assert(item in Item)
        assert(light_type in LightType)

        if item == Item.prism:
            exit(plot_viewangle(3))

        theta = []
        phi = []

        for theta_in0 in range(-89,90):
            theta_in1s = Transposer.__theta_in0_to_theta_in1(theta_in0,item,LP,LPV,flatisout)
            for theta_in1 in theta_in1s:
                theta_AIP_in = Transposer.__theta_in1_to_theta_AIP_in(theta_in1,item,deg)
                if not (-90 < theta_AIP_in < 90):
                    continue
                for phi_in in range(-89,90):
                    phi_AIP_in = Transposer.__phi_in_to_phi_AIP_in(phi_in,item)
                    if not (-90 < phi_AIP_in < 90):
                        continue
                    if recommend:
                        thetaR = radians(theta_AIP_in)
                        phiR = radians(phi_AIP_in)
                        psi = 90 - degrees(acos(1/(tan(thetaR)**2 + tan(phiR)**2 + 1)**(1/2)))
                        if light_type == LightType.I:
                            if not (25 <= psi <= 65):
                                continue
                        else:
                            if 25 <= psi <= 65:
                                continue
                    AIP_dict = {LightType.I:(-theta_AIP_in, -phi_AIP_in), LightType.W:(theta_AIP_in, phi_AIP_in), LightType.X:(phi_AIP_in, theta_AIP_in), LightType.Y:(-phi_AIP_in, -theta_AIP_in)}
                    theta_AIP_out, phi_AIP_out = AIP_dict[light_type]
                    theta_out0 = Transposer.__theta_AIP_out_to_theta_out0(theta_AIP_out, item, deg)
                    phi_out = Transposer.__phi_AIP_out_to_phi_out(phi_AIP_out, item)
                    if not (-90 < theta_out0 < 90):
                        if light_type != LightType.I:
                            theta.append(theta_out0 + deg)
                            phi.append(phi_out)
                    else:
                        theta_out1s = Transposer.__theta_out0_to_theta_out1(theta_out0,item,LP,LPV,flatisout)
                        for theta_out1 in theta_out1s:
                            theta.append(theta_out1 + deg)
                            phi.append(phi_out)
        return theta, phi
            
class Plot:

    def set_item_dict(self, LP=40, LPV=90, deg=45):
        self.__item_dict = {Item.non:"屈折なし", Item.LP:"LP%d_%d"%(LP,deg), Item.LPV:"LPV%d_%d"%(LPV,deg), Item.prism:"直角プリズム", Item.ideal:"理想状態"}

    def common(self, Mdeg, mdeg = None):
        if mdeg is None:
            mdeg = Mdeg
        plt.xlabel("方位角 [deg]", fontname="MS Gothic")
        plt.ylabel("仰角 [deg]", fontname="MS Gothic")
        plt.xlim(-90+mdeg, 90+Mdeg)
        plt.ylim(-90,90)
        plt.legend(prop={"family":"MS Gothic"})
        plt.show()

    def plot_unit(self, light_type:LightType, item:Item, deg = 45, flatisout = True, LP = 40, LPV = 90, recommend = False):
        color_dict = {LightType.I:"tab:blue", LightType.W:"tab:orange", LightType.X:"tab:green", LightType.Y:"tab:red"}
        self.set_item_dict(LP,LPV,deg)
        x,y = Transposer.make_emission_angle_list(item, light_type, deg, LP, LPV, recommend, flatisout)
        plt.scatter(x, y, label=light_type.value, s=5, c=color_dict[light_type])
        plt.title(self.__item_dict[item], fontname="MS Gothic")
        self.common(deg)

    def plot_all_light_type(self, item:Item, deg = 45, flatisout = True, LP = 40, LPV = 90, recommend = False):
        assert(item in Item)
        self.set_item_dict(LP,LPV,deg)
        
        for light_type in LightType:
            x,y = Transposer.make_emission_angle_list(item, light_type, deg, LP, LPV, recommend, flatisout)
            plt.scatter(x, y, label=light_type.value, s=5)
        plt.title(self.__item_dict[item], fontname="MS Gothic")
        self.common(deg)

    def plot_all_item(self, light_type:LightType, deg = 45, flatisout = True, LP = 40, LPV = 90, recommend = False):
        assert(light_type in LightType)
        self.set_item_dict(LP,LPV,deg)

        for item in Item:
            if item == Item.prism:
                print("prismは除く")
                continue
            x,y = Transposer.make_emission_angle_list(item, light_type, deg, LP, LPV, recommend, flatisout)
            plt.scatter(x, y, label=self.__item_dict[item], s=5)    
        plt.title(light_type.value, fontname="MS Gothic")
        self.common(deg)

    def compare_deg(self, item:Item, degs = [45], flatisout = True, LP = 40, LPV = 90, recommend = False):
        assert(item in Item)
        Mdeg = max(degs)
        mdeg = min(degs)
        
        for deg in degs:
            self.set_item_dict(LP,LPV,deg)
            for light_type in LightType:
                x,y = Transposer.make_emission_angle_list(item, light_type, deg, LP, LPV, recommend, flatisout)
                plt.scatter(x, y, label=light_type.value, s=5)
            plt.title(self.__item_dict[item], fontname="MS Gothic")
            self.common(Mdeg,mdeg)

if __name__ == "__main__":
    fig = Plot()
    fig.plot_all_light_type(Item.LP, LP=40, deg=23, flatisout=False)
    # for light_type in LightType:
    #     fig.plot_unit(light_type,Item.non)
    # for i in (30,40):
    #     fig.compare_deg(Item.LP,degs=[30,45,50],LP=i)
    # fig.plot_all_item(LightType.W)
    pass