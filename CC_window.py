# File: CC_window.py
import sys
from PyQt5 import QtWidgets, uic


class CC_window(QtWidgets.QMainWindow):
    """docstring for CC_window"""

    def __init__(self):
        super(CC_window, self).__init__()
        uic.loadUi('./UI/CC.ui', self)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    temp = CC_window()
    app.exec_()
