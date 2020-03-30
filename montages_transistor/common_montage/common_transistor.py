class CommonTransistor(object):
    """
    Common transistor montage
    Class used to calculate:
        Rth: Thevenin equivalent resistance
        Vth : Thevenin equivalent source
        Icq : Polarization current
        Vceq : Collector / Emmiter polarization voltage
        gm : Transconductance of the transistor
        rb : Dynamic base resistance
        r0 : Dynamic collector resistance
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
        super(CommonTransistor, self).__init__()

        # Resistance de polarisation
        self.Rb1 = Rb1
        self.Rb2 = Rb2
        self.Rc = Rc
        self.Re = Re
        self.Rg = Rg
        self.ZL = ZL

        # Condensateur de polarisation
        self.Cg = Cg

        # Parametres des sources
        self.Vcc = Vcc
        self.eg = eg

        # Parametres propre au transistor
        if beta is not None:
            self.beta = beta
        else:
            self.beta = 300
        if Vbe is not None:
            self.Vbe = Vbe
        else:
            self.Vbe = 0.6

        self.UT = 26e-3
        self.VA = 130

    def calcul_thevenin(self):
        self.Rth = R_para(self.Rb1, self.Rb2)
        self.Vth = (self.Rb2 / (self.Rb1 + self.Rb2)) * self.Vcc
        print("Valeurs de thevenin :")
        print("Vth = {}V\nRth = {} Ohms".format(
            round(self.Vth, 2), round(self.Rth, 2)))
        pass

    def calcul_polarisation(self):
        self.Icq = (self.Vth - self.Vbe) / ((self.Rth / self.beta) + self.Re)
        self.Vceq = self.Vcc - (self.Rc + self.Re) * self.Icq
        print("Parametres de polarisation statique")
        print("Icq = {:.2e}A\nVceq = {:.2e}V".format(self.Icq, self.Vceq))
        pass

    def calcul_parametres_dynamiques(self):
        self.gm = self.Icq / self.UT
        self.rb = self.beta * (self.UT / self.Icq)
        self.r0 = self.VA / self.Icq
        print("Parametres de polarisation dynamique :")
        print(("Gm = {:.2e} mA/V\n" +
               "rb = {:.2e} Ohms\n" +
               "r0 = {:.2e} Ohms").format(self.gm * 1e3,
                                          self.rb,
                                          self.r0))
        pass

    def calcul_DDCS(self):
        Ic_max = self.Vcc / (self.Rc + self.Re)
        tab = [[0, self.Vceq, self.Vcc], [Ic_max, self.Icq, 0]]
        return tab

    def __str__(self):
        return ("Rb1 = {}\n" +
                "Rb2 = {}\n" +
                "Rc = {}\n" +
                "Re = {}\n" +
                "Rg = {}\n" +
                "ZL = {}\n" +
                "Cg = {}\n" +
                "Vcc = {}\n" +
                "eg = {}\n" +
                "beta = {}\n" +
                "Vbe = {}\n" +
                "UT = {}\n" +
                "VA = {}").format(self.Rb1,
                                  self.Rb2,
                                  self.Rc,
                                  self.Re,
                                  self.Rg,
                                  self.ZL,
                                  self.Cg,
                                  self.Vcc,
                                  self.eg,
                                  self.beta,
                                  self.Vbe,
                                  self.UT,
                                  self.VA)


def R_para(R1, R2):
    return (R1 * R2) / (R1 + R2)
    pass


if __name__ == "__main__":
    temp = CommonTransistor(Rb1=47e3,
                            Rb2=22e3,
                            Vcc=12,
                            Re=2.2e3,
                            Rc=2.7e3,
                            ZL=100e3,
                            Rg=50)
    temp.calcul_thevenin()
    temp.calcul_polarisation()
    temp.calcul_parametres_dynamiques()
    print(temp)
