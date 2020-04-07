import unittest
import sys
sys.path[0] = "D:\\Bibliothèque\\Documents\\calculus_transistor"
from montages_transistor.common_montage.common_transistor \
    import CommonTransistor


class CommonTransistorTest(unittest.TestCase):
    """Unit tests for CommonTransistor class"""

    def setUp(self):
        self.CT = CommonTransistor(Rb1=47e3,
                                   Rb2=22e3,
                                   Vcc=12,
                                   Re=2.2e3,
                                   Rc=2.7e3,
                                   ZL=100e3,
                                   Rg=50)
        self.CT.calcul_thevenin()
        self.CT.calcul_polarisation()
        self.CT.calcul_parametres_dynamiques()
        pass

    def test_init(self):
        # Defaut value assignement
        self.assertEqual(self.CT.beta, 300)
        self.assertEqual(self.CT.Vbe, 0.6)
        self.assertEqual(self.CT.UT, 26e-3)
        self.assertEqual(self.CT.VA, 130)
        # Value assigned in setUp()
        self.assertEqual(self.CT.Rb1, 47e3)
        self.assertEqual(self.CT.Rb2, 22e3)
        self.assertEqual(self.CT.Vcc, 12)
        self.assertEqual(self.CT.Re, 2.2e3)
        self.assertEqual(self.CT.Rc, 2.7e3)
        self.assertEqual(self.CT.ZL, 100e3)
        self.assertEqual(self.CT.Rg, 50)
        # Value not assigned
        self.assertIsNone(self.CT.Cg)
        self.assertIsNone(self.CT.eg)
        pass

    def test_calcul_thevenin(self):
        self.assertAlmostEqual(self.CT.Vth, 3.83, delta=0.01)
        self.assertAlmostEqual(self.CT.Rth, 14985.51, delta=0.01)
        pass

    def test_calcul_polarisation(self):
        self.assertAlmostEqual(self.CT.Icq, 1.43e-3, delta=0.01)
        self.assertAlmostEqual(self.CT.Vceq, 4.97, delta=0.01)
        pass

    def test_calcul_parametres_dynamiques(self):
        self.assertAlmostEqual(self.CT.gm, 5.51e-3, delta=0.1)
        self.assertAlmostEqual(self.CT.rb, 5.44e3, delta=10)
        self.assertAlmostEqual(self.CT.r0, 9.07e4, delta=100)
        pass

    def test_calcul_DDCS(self):
        tab = self.CT.calcul_DDCS()
        self.assertEqual(tab[0][0], 0)
        self.assertEqual(tab[0][1], self.CT.Vceq)
        self.assertEqual(tab[0][2], self.CT.Vcc)
        self.assertEqual(tab[1][0], 0.0024489795918367346)
        self.assertEqual(tab[1][1], self.CT.Icq)
        self.assertEqual(tab[1][2], 0)
        pass
