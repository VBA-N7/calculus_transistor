import unittest
import sys
sys.path[0] = "D:\\Bibliothèque\\Documents\\calculus_transistor"
from montages_transistor.EC import CommonEmitter


class CommonEmitterTest(unittest.TestCase):
    """Unit tests for CommonEmitter class"""

    def setUp(self):
        self.EC = CommonEmitter(Rb1=180e3,
                                Rb2=15e3,
                                Vcc=20,
                                Re=1e3,
                                Rc=4.7e3,
                                ZL=4.7e3,
                                Rg=50,
                                beta=100,
                                Vbe=0.6)
        self.EC.calcul_thevenin()
        self.EC.calcul_polarisation()
        self.EC.calcul_parametres_dynamiques()
        pass

    def test_calcul_ZE(self):
        self.EC.calcul_ZE()
        self.assertAlmostEqual(self.EC.ZE, 2568.9, delta=0.1)
        pass

    def test_calcul_ZS(self):
        self.EC.calcul_ZS()
        self.assertAlmostEqual(self.EC.ZS, 4563.9, delta=0.1)
        pass

    def test_AV(self):
        self.EC.calcul_gain_intrinseque()
        self.assertAlmostEqual(self.EC.AV, -73.4, delta=0.1)
        pass

    def test_GV(self):
        self.EC.calcul_ZE()
        self.EC.calcul_gain_intrinseque()
        self.EC.calcul_gain_composite()
        self.assertAlmostEqual(self.EC.GV, -72, delta=0.1)
        pass

    def test_DDCD(self):
        tab = self.EC.calcul_DDCD()
        self.assertEqual(tab[0][0], 0)
        self.assertEqual(tab[0][1], self.EC.Vceq)
        self.assertAlmostEqual(tab[0][2], 17.21007120672886)
        self.assertAlmostEqual(tab[1][0], 0.007432562866201451)
        self.assertEqual(tab[1][1], self.EC.Icq)
        self.assertEqual(tab[1][2], 0)
        pass

    def test_calcul_dynamic_limits(self):
        tab = self.EC.calcul_dynamic_limits()
        self.assertAlmostEqual(tab[0], 13.392631495973841)
        self.assertAlmostEqual(tab[1], 17.21007120672886)
        self.assertAlmostEqual(tab[2], 0)
        self.assertAlmostEqual(tab[3], 0.0016486486486486486)
        pass
