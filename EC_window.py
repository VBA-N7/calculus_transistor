# File: EC_window.py
import sys
from PyQt5 import QtWidgets, uic
from montages_transistor.EC import CommonEmitter
import matplotlib.pyplot as plt


class EC_window(QtWidgets.QMainWindow):
    """docstring for EC_window"""

    def __init__(self):
        super(EC_window, self).__init__()
        uic.loadUi('./UI/EC.ui', self)

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

        self.spin_ZL_V = self.findChild(QtWidgets.QDoubleSpinBox, 'ZL_V')
        self.combo_ZL_E = self.findChild(QtWidgets.QComboBox, 'ZL_E')

        self.spin_Vcc_V = self.findChild(QtWidgets.QDoubleSpinBox, 'Vcc_V')
        self.combo_Vcc_E = self.findChild(QtWidgets.QComboBox, 'Vcc_E')

        self.spin_beta_V = self.findChild(QtWidgets.QDoubleSpinBox, 'beta_V')

    def start_calculus(self):
        self.EC = CommonEmitter()
        self.get_parameters()
        self.EC.calcul_thevenin()
        self.EC.calcul_polarisation()
        self.EC.calcul_parametres_dynamiques()
        self.EC.calcul_ZE()
        self.EC.calcul_ZS()
        self.EC.calcul_gain_intrinseque()
        self.EC.calcul_gain_composite()
        self.display_results()
        self.BP_DDC.setEnabled(True)
        pass

    def get_parameters(self):
        self.EC.eg = self.spin_eg_V.value() * \
            self.index_to_exponant_volt(self.combo_eg_E)
        self.EC.Vcc = self.spin_Vcc_V.value() * \
            self.index_to_exponant_volt(self.combo_Vcc_E)

        self.EC.Rg = self.spin_Rg_V.value() * \
            self.index_to_exponant_ohm(self.combo_Rg_E)
        self.EC.Rb1 = self.spin_Rb1_V.value() * \
            self.index_to_exponant_ohm(self.combo_Rb1_E)
        self.EC.Rb2 = self.spin_Rb2_V.value() * \
            self.index_to_exponant_ohm(self.combo_Rb2_E)
        self.EC.Rc = self.spin_Rc_V.value() * \
            self.index_to_exponant_ohm(self.combo_Rc_E)
        self.EC.Re = self.spin_Re_V.value() * \
            self.index_to_exponant_ohm(self.combo_Re_E)
        self.EC.ZL = self.spin_ZL_V.value() * \
            self.index_to_exponant_ohm(self.combo_ZL_E)
        self.EC.beta = self.spin_beta_V.value()

        print(self.EC.eg)
        print(self.EC.Vcc)
        print(self.EC.Rg)
        print(self.EC.Rb1)
        print(self.EC.Rb2)
        print(self.EC.Rc)
        print(self.EC.Re)
        print(self.EC.ZL)
        print(self.EC.beta)
        pass

    def display_results(self):
        self.L_vth.setText("{}".format(round(self.EC.Vth, 2)))
        self.L_rth.setText("{:.2e}".format(self.EC.Rth, 1))
        self.L_icq.setText("{:.2e}".format(self.EC.Icq))
        self.L_vceq.setText("{:.2e}".format(self.EC.Vceq))

        self.L_gm.setText("{:.2e}".format(self.EC.gm))
        self.L_rb.setText("{:.2e}".format(self.EC.rb))
        self.L_r0.setText("{:.2e}".format(self.EC.r0))
        self.L_ze.setText("{:.2e}".format(self.EC.ZE))
        self.L_zs.setText("{:.2e}".format(self.EC.ZS))
        self.L_av.setText("{}".format(round(self.EC.AV, 2)))
        self.L_gv.setText("{}".format(round(self.EC.GV, 2)))
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
        plt.plot(self.EC.calcul_DDCS()[0], self.EC.calcul_DDCS()[1], "g-o")
        plt.plot(self.EC.calcul_DDCD()[0], self.EC.calcul_DDCD()[1], "r-x")
        plt.xlabel('Vce (V)')
        plt.ylabel('Ic (A)')
        plt.title('Droite de charge')
        plt.legend(["Statique", "Dynamique"])
        plt.grid()
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        plt.annotate(s="Point de polarisation",
                     xy=(self.EC.Vceq,
                         self.EC.Icq))
        plt.annotate(s="Icmax: {:.2e}".format(self.EC.calcul_DDCS()[1][0]),
                     xy=(self.EC.calcul_DDCS()[0][0],
                         self.EC.calcul_DDCS()[1][0]))
        plt.annotate(s="icmax: {:.2e}".format(self.EC.calcul_DDCD()[1][0]),
                     xy=(self.EC.calcul_DDCD()[0][0],
                         self.EC.calcul_DDCD()[1][0]))
        plt.annotate(s="vcemax: {}".format(round(self.EC.calcul_DDCD()[0][2],
                                                 2)),
                     xy=(self.EC.calcul_DDCD()[0][2],
                         self.EC.calcul_DDCD()[1][2]))

        xmin, xmax, ymin, ymax = self.EC.calcul_dynamic_limits()
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

        plt.annotate("",
                     xy=(xmin, ymin),
                     xytext=(xmin, ymax),
                     arrowprops=dict(arrowstyle="<->"))
        plt.annotate("Δic",
                     xy=(0, 0),
                     xytext=(xmin, self.EC.Icq))

        plt.annotate("",
                     xy=(xmin, ymin),
                     xytext=(xmax, ymin),
                     arrowprops=dict(arrowstyle="<->"))
        plt.annotate("Δvce",
                     xy=(0, 0),
                     xytext=(self.EC.Vceq,
                             ymin))
        plt.show()
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    temp = EC_window()
    temp.show()
    app.exec_()
