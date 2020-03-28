# File: main.py
import sys
from PyQt5 import QtWidgets, uic
from CC_window import CC_window


class main_window(QtWidgets.QMainWindow):
    """docstring for main_window"""

    def __init__(self):
        super(main_window, self).__init__()
        uic.loadUi('./UI/mainwindow.ui', self)

        self.choix_montage = self.findChild(QtWidgets.QComboBox,
                                            'choix_montage')
        self.valide_choix = self.findChild(QtWidgets.QPushButton,
                                           'BP_valide_choix')
        self.quitter = self.findChild(QtWidgets.QPushButton,
                                      'BP_quitter')

        self.valide_choix.clicked.connect(self.BP_valide_choix_handler)
        self.quitter.clicked.connect(self.BP_quitter_handler)

    def BP_valide_choix_handler(self):
        index_choix = self.choix_montage.currentIndex()

        if index_choix == 0:
            self.window_montage = CC_window()
            self.window_montage.show()
            self.hide()
            pass

        pass

    def BP_quitter_handler(self):
        sys.exit()
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    temp = main_window()
    temp.show()
    app.exec_()
