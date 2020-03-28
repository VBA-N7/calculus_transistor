try:
    from montages_transistor.common_montage.common_transistor \
        import CommonTransistor
except Exception:
    from common_montage.common_transistor import CommonTransistor


class CommonBase(CommonTransistor):
    """
    Common Base montage
    Class used to calculate:
        ZE: input impedance
        AV: intrinsic gain
        GV: voltage gain
    """

    def __init__(self,
                 Rb1=None,
                 Rb2=None,
                 Rc=None,
                 Re=None,
                 Rg=None,
                 Cg=None,
                 Vcc=None,
                 eg=None,
                 beta=None,
                 Vbe=None,
                 ZL=None):
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
        self.ZE = 1 / (self.gm)
        print("Impédance entrée BC = {:.2e} Ohms".format(self.ZE))
        pass

    def calcul_gain_intrinseque(self):
        self.AV = self.gm * R_para(self.Rc, self.ZL)
        print("Gain intrinseque BC = {}".format(round(self.AV, 2)))
        pass

    def calcul_gain_composite(self):
        self.GV = (self.ZE * self.AV) / (self.ZE + self.Rg)
        print("Gain composite BC = {}".format(round(self.GV, 2)))
        pass

    def __str__(self):
        parent = super().__str__()
        return "{}\nZE: {:.2e}\nAV: {:.2e}\nGV: {:.2e}".format(parent,
                                                               self.ZE,
                                                               self.AV,
                                                               self.GV)


def R_para(R1, R2):
    return (R1 * R2) / (R1 + R2)
    pass


if __name__ == "__main__":
    temp = CommonBase(Rb1=47e3,
                      Rb2=22e3,
                      Rc=2.7e3,
                      Re=2.2e3,
                      ZL=100e3,
                      Vcc=12,
                      Rg=50)
    temp.calcul_thevenin()
    temp.calcul_polarisation()
    temp.calcul_parametres_dynamiques()
    temp.calcul_ZE()
    temp.calcul_gain_intrinseque()
    temp.calcul_gain_composite()
    print(temp)
