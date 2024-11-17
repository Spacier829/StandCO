from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QLabel

from standco.src.connection_manager import ConnectionManager
from standco.src.sensor_manager import SensorManager


class Stand_Gui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stand GUI")
        self.setGeometry(1000, 500, 600, 200)
        # self.setup_ui()
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        self.sensor_status_widgets = []
        self.connection_manager = ConnectionManager()
        self.sensor_manager = SensorManager(
            [{"sensors": device["sensors"]} for device in self.connection_manager.clients])
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_sensor_states)
        self.timer.start(1000)

    # def setup_ui(self):
    #     main_layout = QtWidgets.QVBoxLayout()
    #     main_layout.setContentsMargins(0, 0, 0, 0)
    #     # self.button = QtWidgets.QPushButton("Start", self)
    #     # self.button.clicked.connect(self.get_modbus_status)
    #     # main_layout.addWidget(self.button)
    #     main_layout.addWidget(self.create_sensor_widgets())
    #     self.setLayout(main_layout)

    def create_sensor_widgets(self):
        for sensor in self.sensor_manager.get_sensors_states():
            groupbox = QtWidgets.QGroupBox(sensor["name"])
            hbox = QtWidgets.QHBoxLayout()

            status_label = QLabel(sensor["name"])
            status_label.setPixmap(self.create_circle_pixmap(QtGui.QColor('gray')))
            hbox.addWidget(status_label)

            groupbox.setLayout(hbox)
            self.sensor_status_widgets.append(status_label)
            self.layout.addWidget(groupbox)
            # return groupbox

    def update_sensor_states(self):
        states = self.connection_manager.read_sensors()
        self.sensor_manager.update_sensors_states(states)

        for i, sensor in enumerate(self.sensor_manager.get_sensors_states()):
            color = QtGui.QColor('green') if sensor["state"] else QtGui.QColor('gray')
            self.sensor_status_widgets[i].setPixmap(self.create_circle_pixmap(color))

    def create_circle_pixmap(self, color, size=20):
        pixmap = QtGui.QPixmap(size, size)
        pixmap.fill(QtGui.QColor('transparent'))
        painter = QtGui.QPainter(pixmap)
        painter.setBrush(color)
        painter.setPen(QtGui.QColor('black'))
        painter.drawEllipse(0, 0, size - 1, size - 1)
        painter.end()
        return pixmap

    def closeEvent(self, event):
        self.connection_manager.close()
        event.accept()
