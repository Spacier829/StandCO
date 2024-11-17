from PyQt6 import QtWidgets
import sys
from stand_gui import Stand_Gui
from connection_manager import ConnectionManager

if __name__ == '__main__':
    # app = QtWidgets.QApplication(sys.argv)
    # win = Stand_Gui()
    # win.show()
    # app.exec()
    connection_manager = ConnectionManager()
    connection_manager.read_sensors()
    a = 123;