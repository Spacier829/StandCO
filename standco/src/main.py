from PyQt6 import QtWidgets
import sys
from standco.src.gui.stand_gui import StandGui

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = StandGui()
    win.show()
    sys.exit(app.exec())
