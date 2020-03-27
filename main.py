# File: main.py
import sys
from PyQt5 import QtWidgets, uic


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

        self.show()

    def BP_valide_choix_handler(self):
        index_choix = self.choix_montage.currentIndex()
        text_choix = self.choix_montage.currentText()
        print(text_choix, index_choix)

        pass

    def BP_quitter_handler(self):
        sys.exit()
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    temp = main_window()
    app.exec_()
