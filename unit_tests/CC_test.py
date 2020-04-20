import unittest
import sys
sys.path[0] = "D:\\Bibliothèque\\Documents\\calculus_transistor"
from montages_transistor.CC import CommonCollector


class CommonCollectorTest(unittest.TestCase):
    """Unit tests for CommonCollector class"""

    def setUp(self):
        self.CC = CommonCollector(Rb1=47e3,
                                  Rb2=47e3,
                                  Re=3.3e3,
                                  Rc=150,
                                  ZL=100e3,
                                  Vcc=12,
                                  beta=100,
                                  Rg=50)
        self.CC.calcul_thevenin()
        self.CC.calcul_polarisation()
        self.CC.calcul_parametres_dynamiques()
        pass

    def test_calcul_ZE(self):
        self.CC.calcul_ZE()
        self.assertAlmostEqual(self.CC.ZE, 21897.7, delta=0.1)
        pass

    def test_calcul_ZS(self):
        self.CC.calcul_ZS()
        self.assertAlmostEqual(self.CC.ZS, 17.42, delta=0.1)
        pass

    def test_AV(self):
        self.CC.calcul_gain_intrinseque()
        self.assertAlmostEqual(self.CC.AV, 1, delta=0.1)
        pass

    def test_GV(self):
        self.CC.calcul_ZE()
        self.CC.calcul_gain_intrinseque()
        self.CC.calcul_gain_composite()
        self.assertAlmostEqual(self.CC.GV, 1, delta=0.1)
        pass

    def test_DDCD(self):
        tab = self.CC.calcul_DDCD()
        self.assertEqual(tab[0][0], 0)
        self.assertEqual(tab[0][1], self.CC.Vceq)
        self.assertAlmostEqual(tab[0][2], 11.60982349099244)
        self.assertAlmostEqual(tab[1][0], 0.003634226565513695)
        self.assertEqual(tab[1][1], self.CC.Icq)
        self.assertEqual(tab[1][2], 0)
        pass

    def test_calcul_dynamic_limits(self):
        tab = self.CC.calcul_dynamic_limits()
        self.assertAlmostEqual(tab[0], 1.8498653350330194)
        self.assertAlmostEqual(tab[1], 11.60982349099244)
        self.assertAlmostEqual(tab[2], 0)
        self.assertAlmostEqual(tab[3], 0.0030551626591230553)
        pass
