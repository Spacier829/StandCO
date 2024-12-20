from PyQt6 import QtWidgets
import sys
from standco.src.gui.stand_gui import Stand_Gui

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Stand_Gui()
    win.show()
    sys.exit(app.exec())
