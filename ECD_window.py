# File: ECD_window.py
import sys
from PyQt5 import QtWidgets, uic
from montages_transistor.ECD import CommonEmitterDegenerate
import matplotlib.pyplot as plt


class ECD_window(QtWidgets.QMainWindow):
    """docstring for ECD_window"""

    def __init__(self):
        super(ECD_window, self).__init__()
        uic.loadUi('./UI/ECD.ui', self)

        self.BP_start_calculus = self.findChild(QtWidgets.QPushButton,
                                                'BP_start_calculus')
        self.BP_start_calculus.clicked.connect(self.start_calculus)

        self.BP_DDC = self.findChild(QtWidgets.QPushButton, 'BP_DDC')
        self.BP_DDC.clicked.connect(self.display_DDC)

        self.L_vth = self.findChild(QtWidgets.QLineEdit, 'L_vth')
        self.L_rth = self.findChild(QtWidgets.QLineEdit, 'L_rth')
        self.L_icq = self.findChild(QtWidgets.QLineEdit, 'L_icq')
        self.L_vceq = self.findChild(QtWidgets.QLineEdit, 'L_vceq')

        self.L_gm = self.findChild(QtWidgets.QLineEdit, 'L_gm')
        self.L_rb = self.findChild(QtWidgets.QLineEdit, 'L_rb')
        self.L_r0 = self.findChild(QtWidgets.QLineEdit, 'L_r0')
        self.L_ze = self.findChild(QtWidgets.QLineEdit, 'L_ze')
        self.L_zs = self.findChild(QtWidgets.QLineEdit, 'L_zs')
        self.L_av = self.findChild(QtWidgets.QLineEdit, 'L_av')
        self.L_gv = self.findChild(QtWidgets.QLineEdit, 'L_gv')

        self.spin_eg_V = self.findChild(QtWidgets.QDoubleSpinBox, 'eg_V')
        self.combo_eg_E = self.findChild(QtWidgets.QComboBox, 'eg_E')

        self.spin_Rg_V = self.findChild(QtWidgets.QDoubleSpinBox, 'Rg_V')
        self.combo_Rg_E = self.findChild(QtWidgets.QComboBox, 'Rg_E')

        self.spin_Rb1_V = self.findChild(QtWidgets.QDoubleSpinBox, 'Rb1_V')
        self.combo_Rb1_E = self.findChild(QtWidgets.QComboBox, 'Rb1_E')

        self.spin_Rb2_V = self.findChild(QtWidgets.QDoubleSpinBox, 'Rb2_V')
        self.combo_Rb2_E = self.findChild(QtWidgets.QComboBox, 'Rb2_E')

        self.spin_Rc_V = self.findChild(QtWidgets.QDoubleSpinBox, 'Rc_V')
        self.combo_Rc_E = self.findChild(QtWidgets.QComboBox, 'Rc_E')

        self.spin_Re_V = self.findChild(QtWidgets.QDoubleSpinBox, 'Re_V')
        self.combo_Re_E = self.findChild(QtWidgets.QComboBox, 'Re_E')

        self.spin_Re0_V = self.findChild(QtWidgets.QDoubleSpinBox, 'Re0_V')
        self.combo_Re0_E = self.findChild(QtWidgets.QComboBox, 'Re0_E')

        self.spin_ZL_V = self.findChild(QtWidgets.QDoubleSpinBox, 'ZL_V')
        self.combo_ZL_E = self.findChild(QtWidgets.QComboBox, 'ZL_E')

        self.spin_Vcc_V = self.findChild(QtWidgets.QDoubleSpinBox, 'Vcc_V')
        self.combo_Vcc_E = self.findChild(QtWidgets.QComboBox, 'Vcc_E')

        self.spin_beta_V = self.findChild(QtWidgets.QDoubleSpinBox, 'beta_V')

    def start_calculus(self):
        self.ECD = CommonEmitterDegenerate()
        self.get_parameters()
        self.ECD.calcul_thevenin()
        self.ECD.calcul_polarisation()
        self.ECD.calcul_parametres_dynamiques()
        self.ECD.calcul_ZE()
        self.ECD.calcul_ZS()
        self.ECD.calcul_gain_intrinseque()
        self.ECD.calcul_gain_composite()
        self.display_results()
        self.BP_DDC.setEnabled(True)
        pass

    def get_parameters(self):
        self.ECD.eg = self.spin_eg_V.value() * \
            self.index_to_exponant_volt(self.combo_eg_E)
        self.ECD.Vcc = self.spin_Vcc_V.value() * \
            self.index_to_exponant_volt(self.combo_Vcc_E)

        self.ECD.Rg = self.spin_Rg_V.value() * \
            self.index_to_exponant_ohm(self.combo_Rg_E)
        self.ECD.Rb1 = self.spin_Rb1_V.value() * \
            self.index_to_exponant_ohm(self.combo_Rb1_E)
        self.ECD.Rb2 = self.spin_Rb2_V.value() * \
            self.index_to_exponant_ohm(self.combo_Rb2_E)
        self.ECD.Rc = self.spin_Rc_V.value() * \
            self.index_to_exponant_ohm(self.combo_Rc_E)
        self.ECD.Re = self.spin_Re_V.value() * \
            self.index_to_exponant_ohm(self.combo_Re_E)
        self.ECD.Re0 = self.spin_Re0_V.value() * \
            self.index_to_exponant_ohm(self.combo_Re0_E)
        self.ECD.ZL = self.spin_ZL_V.value() * \
            self.index_to_exponant_ohm(self.combo_ZL_E)
        self.ECD.beta = self.spin_beta_V.value()

        print(self.ECD.eg)
        print(self.ECD.Vcc)
        print(self.ECD.Rg)
        print(self.ECD.Rb1)
        print(self.ECD.Rb2)
        print(self.ECD.Rc)
        print(self.ECD.Re)
        print(self.ECD.Re0)
        print(self.ECD.ZL)
        print(self.ECD.beta)
        pass

    def display_results(self):
        self.L_vth.setText("{}".format(round(self.ECD.Vth, 2)))
        self.L_rth.setText("{:.2e}".format(self.ECD.Rth, 1))
        self.L_icq.setText("{:.2e}".format(self.ECD.Icq))
        self.L_vceq.setText("{:.2e}".format(self.ECD.Vceq))

        self.L_gm.setText("{:.2e}".format(self.ECD.gm))
        self.L_rb.setText("{:.2e}".format(self.ECD.rb))
        self.L_r0.setText("{:.2e}".format(self.ECD.r0))
        self.L_ze.setText("{:.2e}".format(self.ECD.ZE))
        self.L_zs.setText("{:.2e}".format(self.ECD.ZS))
        self.L_av.setText("{}".format(round(self.ECD.AV, 2)))
        self.L_gv.setText("{}".format(round(self.ECD.GV, 2)))
        pass

    def index_to_exponant_volt(self, combo_box):
        if combo_box.currentIndex() == 0:
            return 1e-3
        else:
            return 1
        pass

    def index_to_exponant_ohm(self, combo_box):
        n = (-6 + (combo_box.currentIndex() * 3))
        return pow(10, n)
        pass

    def display_DDC(self):
        plt.close('all')
        plt.figure(1)
        plt.plot(self.ECD.calcul_DDCS()[0], self.ECD.calcul_DDCS()[1], "g-o")
        plt.plot(self.ECD.calcul_DDCD()[0], self.ECD.calcul_DDCD()[1], "r-x")
        plt.xlabel('Vce (V)')
        plt.ylabel('Ic (A)')
        plt.title('Droite de charge statique & dynamique')
        plt.grid()
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        plt.annotate(s="Point de polarisation",
                     xy=(self.ECD.Vceq, self.ECD.Icq))

        xmin, xmax, ymin, ymax = self.ECD.calcul_dynamic_limits()
        plt.axvspan(xmin,
                    xmax,
                    ymin=0,
                    ymax=1,
                    alpha=0.2)
        plt.axvline(xmin, linestyle="dotted")
        plt.axvline(xmax, linestyle="dotted")

        plt.axhspan(ymin,
                    ymax,
                    xmin=0,
                    xmax=1,
                    alpha=0.2,
                    facecolor='g')
        plt.axhline(ymin, linestyle="dotted", color='g')
        plt.axhline(ymax, linestyle="dotted", color='g')
        plt.show()
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    temp = ECD_window()
    temp.show()
    app.exec_()
