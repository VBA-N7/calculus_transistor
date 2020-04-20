import unittest
import sys
sys.path[0] = "D:\\Bibliothèque\\Documents\\calculus_transistor"
from montages_transistor.ECD import CommonEmitterDegenerate


class CommonEmitterTest(unittest.TestCase):
    """Unit tests for CommonEmitterDegenerate class"""

    def setUp(self):
        self.ECD = CommonEmitterDegenerate(Rb1=180e3,
                                           Rb2=15e3,
                                           Vcc=20,
                                           Re=1e3,
                                           Rc=4.7e3,
                                           ZL=4.7e3,
                                           Rg=50,
                                           beta=100,
                                           Re0=203)
        self.ECD.calcul_thevenin()
        self.ECD.calcul_polarisation()
        self.ECD.calcul_parametres_dynamiques()
        pass

    def test_calcul_ZE(self):
        self.ECD.calcul_ZE()
        self.assertAlmostEqual(self.ECD.ZE, 8706.3, delta=0.1)
        pass

    def test_calcul_ZS(self):
        self.ECD.calcul_ZS()
        self.assertAlmostEqual(self.ECD.ZS, 4700, delta=0.1)
        pass

    def test_AV(self):
        self.ECD.calcul_gain_intrinseque()
        self.assertAlmostEqual(self.ECD.AV, -10, delta=0.1)
        pass

    def test_GV(self):
        self.ECD.calcul_ZE()
        self.ECD.calcul_gain_intrinseque()
        self.ECD.calcul_gain_composite()
        self.assertAlmostEqual(self.ECD.GV, -10, delta=0.1)
        pass

    def test_DDCD(self):
        tab = self.ECD.calcul_DDCD()
        self.assertEqual(tab[0][0], 0)
        self.assertEqual(tab[0][1], self.ECD.Vceq)
        self.assertAlmostEqual(tab[0][2], 19.175675675675674)
        self.assertAlmostEqual(tab[1][0], 0.004079930994824611)
        self.assertEqual(tab[1][1], self.ECD.Icq)
        self.assertEqual(tab[1][2], 0)
        pass

    def test_calcul_dynamic_limits(self):
        tab = self.ECD.calcul_dynamic_limits()
        self.assertAlmostEqual(tab[0], 11.427027027027027)
        self.assertAlmostEqual(tab[1], 19.175675675675674)
        self.assertAlmostEqual(tab[2], 0.0)
        self.assertAlmostEqual(tab[3], 0.0016486486486486486)
        pass
