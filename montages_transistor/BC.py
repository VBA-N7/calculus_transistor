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
        self.AV = self.gm / ((1 / self.r0) + (1 / self.Rc) + (1 / self.ZL))
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

    def calcul_DDCD(self):
        Q = (self.Vceq, self.Icq)
        coeff_dir = (- 1) / (R_para(R_para(self.r0, self.ZL), self.Rc))
        A = (0, coeff_dir * (- Q[0]) + Q[1])
        B = (Q[0] - (Q[1] / coeff_dir), 0)
        return [[A[0], self.Vceq, B[0]], [A[1], self.Icq, B[1]]]
        pass

    def calcul_dynamic_limits(self):
        xDistance_Q_to_origin = self.Vceq
        xDistance_Q_to_DDCD = self.calcul_DDCD()[0][2] - self.Vceq
        xDistance_Q_to_DDCS = self.Vcc - self.Vceq
        tab = [xDistance_Q_to_origin, xDistance_Q_to_DDCD, xDistance_Q_to_DDCS]
        xmin = self.Vceq - min(tab)
        xmax = self.Vceq + min(tab)

        yDistance_Q_to_origin = self.Icq
        yDistance_Q_to_DDCD = self.calcul_DDCD()[1][0] - self.Icq
        yDistance_Q_to_DDCS = self.calcul_DDCS()[1][0] - self.Icq
        tab = [yDistance_Q_to_origin, yDistance_Q_to_DDCD, yDistance_Q_to_DDCS]
        ymin = self.Icq - min(tab)
        ymax = self.Icq + min(tab)

        return xmin, xmax, ymin, ymax


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
    temp.calcul_DDCD()
    print(temp)
