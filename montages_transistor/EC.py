from common_transistor import CommonTransistor


class CommonEmitter(CommonTransistor):
    """
    Common Emitter montage
    Class used to calculate:
        ZE: input impedance
        ZS: output impedance
        AV: intrinsic gain
        GV: voltage gain
    """

    def __init__(self,
                 Rb1=None,
                 Rb2=None,
                 Rc=None,
                 Re=None,
                 Rg=None,
                 ZL=None,
                 Cg=None,
                 Vcc=None,
                 eg=None,
                 beta=None,
                 Vbe=None):
        super().__init__(Rb1,
                         Rb2,
                         Rc,
                         Re,
                         Rg,
                         ZL,
                         Cg,
                         Vcc,
                         eg,
                         beta,
                         Vbe)

    def calcul_ZE(self):
        #  self.calcul_parametress_dynamiques()
        self.ZE = 1 / ((1 / self.Rb1) + (1 / self.Rb2) + (1 / self.Rth))
        print("Impédance entrée EC = {:.2e} Ohms".format(self.ZE))

    def calcul_ZS(self):
        #  self.calcul_parametres_dynamiques()
        self.ZS = 1 / ((1 / self.r0) + (1 / self.Rc))
        print("Impédance sortie EC = {:.2e} Ohms".format(self.ZE))

    def calcul_gain_intrinseque(self):
        #  self.calcul_parametres_dynamiques()
        self.AV = self.gm / ((1 / self.r0) + (1 / self.Rc) + (1 / self.ZL))
        print("Gain intrinseque EC = {}".format(round(self.AV, 2)))

    def calcul_gain_composite(self):
        #  self.calcul_parametres_dynamiques()
        self.GV = self.AV * self.ZE / (self.ZE + self.Rg)
        print("Gain composite EC = {}".format(round(self.GV, 2)))

    def __str__(self):
        parent = super().__str__()
        return "{}\nZE: {}\nZS: {}\nAV: {}\nGV: {}".format(parent,
                                                           self.ZE,
                                                           self.ZS,
                                                           self.AV,
                                                           self.GV)


if __name__ == "__main__":
    test = CommonEmitter(Rb1=47e3,
                         Rb2=22e3,
                         Vcc=12,
                         Re=2.2e3,
                         Rc=2.7e3,
                         ZL=100e3,
                         Rg=50)

    test.calcul_thevenin()
    test.calcul_polarisation()
    test.calcul_parametres_dynamiques()
    test.calcul_ZE()
    test.calcul_ZS()
    test.calcul_gain_intrinseque()
    test.calcul_gain_composite()
    print(test)
