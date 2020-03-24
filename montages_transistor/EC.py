from .common_transistor import CommonTransistor


class CommonEmitter(CommonTransistor):
    """
    Common Emitter montage
    Class used to calculate:
        Zin: input impedance
        Zout: output impedance
        Av: intrinsic gain
        Gv: voltage gain
    """
    def __init__(self, rb1=None, rb2=None, rc=None, re=None, rg=None, zl=None, cg=None, vcc=None, eg=None, beta=None, vbe=None):
        super().__init__(rb1, rb2, rc, re, rg, zl, cg, vcc, eg, beta, vbe)

        self.Zin = self.set_zin()
        self.Zout = self.set_zout()
        self.Av = self.set_av()
        self.Gv = self.set_gv()

    def set_zin(self):
        #  self.calcul_parametress_dynamiques()
        return 1/((1/self.Rb1) + (1/self.Rb2) + (1/self.rb))

    def set_zout(self):
        #  self.calcul_parametres_dynamiques()
        return 1/((1/self.r0)+(1/self.Rc))

    def set_av(self):
        #  self.calcul_parametres_dynamiques()
        return self.gm/((1/self.r0) + (1/self.Rc) + (1/self.Zl))

    def set_gv(self):
        #  self.calcul_parametres_dynamiques()
        return self.Av*self.Zin/(self.Zin + self.Rg)

    def test(self):
        print("Ze: {}".format(self.Zin))
        print("Zs: {}".format(self.Zout))
        print("Av: {}".format(self.Av))
        print("Gv: {}".format(self.Gv))


if __name__ == "__main__":
    test = CommonEmitter(rb1=47e3, rb2=22e3, vcc=12, re=2.2e3, rc=2.7e3, zl=100e3, rg=50)
    test.test()