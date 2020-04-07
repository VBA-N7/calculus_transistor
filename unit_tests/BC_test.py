import unittest
import sys
sys.path[0] = "D:\\Bibliothèque\\Documents\\calculus_transistor"
from montages_transistor.BC import CommonBase


class CommonBaseTest(unittest.TestCase):
    """Unit tests for CommonBase class"""

    def setUp(self):
        self.BC = CommonBase(Rb1=47e3,
                             Rb2=22e3,
                             Rc=2.7e3,
                             Re=2.2e3,
                             ZL=100e3,
                             Vcc=12,
                             Rg=50)
        self.BC.calcul_thevenin()
        self.BC.calcul_polarisation()
        self.BC.calcul_parametres_dynamiques()
        pass

    def test_calcul_ZE(self):
        self.BC.calcul_ZE()
        self.assertAlmostEqual(self.BC.ZE, 18.1, delta=0.1)
        pass

    def test_AV(self):
        self.BC.calcul_gain_intrinseque()
        self.assertAlmostEqual(self.BC.AV, 140.9, delta=0.01)
        pass

    def test_GV(self):
        self.BC.calcul_ZE()
        self.BC.calcul_gain_intrinseque()
        self.BC.calcul_gain_composite()
        self.assertAlmostEqual(self.BC.GV, 37.5, delta=0.01)
        pass

    def test_DDCD(self):
        tab = self.BC.calcul_DDCD()
        self.assertEqual(tab[0][0], 0)
        self.assertEqual(tab[0][1], self.BC.Vceq)
        self.assertAlmostEqual(tab[0][2], 8.637529713321277)
        self.assertAlmostEqual(tab[1][0], 0.003380728821436684)
        self.assertEqual(tab[1][1], self.BC.Icq)
        self.assertEqual(tab[1][2], 0)
        pass

    def test_calcul_dynamic_limits(self):
        tab = self.BC.calcul_dynamic_limits()
        self.assertAlmostEqual(tab[0], 1.3107676199548006)
        self.assertAlmostEqual(tab[1], 8.637529713321277)
        self.assertAlmostEqual(tab[2], 0.0004187148299436578)
        self.assertAlmostEqual(tab[3], 0.0024489795918367346)
        pass
