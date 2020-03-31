try:
    from montages_transistor.common_montage.common_transistor \
        import CommonTransistor
except Exception:
    from common_montage.common_transistor import CommonTransistor


class CommonCollector(CommonTransistor):
    """
    Common Collector montage
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
        re = self.rb + (self.beta * R_para(self.Re, self.ZL))
        self.ZE = R_para(re, self.Rth)
        print("Impédance entrée CC = {:.2e} Ohms".format(self.ZE))
        pass

    def calcul_ZS(self):
        tampon = (self.rb + R_para(self.Rg, self.Rth)) / self.beta
        self.ZS = R_para(self.Re, tampon)
        print("Impédance sortie CC = {:.2e} Ohms".format(self.ZS))
        pass

    def calcul_gain_intrinseque(self):
        self.AV = (self.gm * R_para(self.Re, self.ZL)) / \
            (1 + (self.gm * R_para(self.Re, self.ZL)))
        print("Gain intrinseque CC = {}".format(round(self.AV, 2)))
        pass

    def calcul_gain_composite(self):
        self.GV = self.AV * self.ZE / (self.ZE + self.Rg)
        print("Gain composite CC = {}".format(round(self.GV, 2)))
        pass

    def __str__(self):
        parent = super().__str__()
        return "{}\nZE: {}\nZS: {}\nAV: {}\nGV: {}".format(parent,
                                                           self.ZE,
                                                           self.ZS,
                                                           self.AV,
                                                           self.GV)

    def calcul_DDCD(self):
        Q = (self.Vceq, self.Icq)
        coeff_dir = (- 1) / R_para(self.Re, self.ZL)
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
    test = CommonCollector(Rb1=47e3,
                           Rb2=47e3,
                           Re=3.3e3,
                           Rc=150,
                           ZL=100e3,
                           Vcc=12,
                           beta=100,
                           Rg=50)
    test.calcul_thevenin()
    test.calcul_polarisation()
    test.calcul_parametres_dynamiques()
    test.calcul_ZE()
    test.calcul_ZS()
    test.calcul_gain_intrinseque()
    test.calcul_gain_composite()
    test.calcul_DDCD()
    print(test)
