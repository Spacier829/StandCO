from PyQt6 import QtWidgets, QtGui, QtCore
from standco.src.gui.graphs.graph_plot import GraphPlot
from standco.src.gui.indicators.relay_indicator import RelayIndicator
from standco.src.managers.connection_manager import ConnectionManager
from standco.src.managers.relay_manager import RelayManager
from standco.src.managers.sensor_manager import SensorManager
from standco.src.managers.sensor_manager import SensorManager
from standco.src.states_reader.states_reader import StatesReader
from datetime import datetime


class StandGui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.sensors = []
        self.relays = []
        self.p_data = 1
        self.t_data = -1
        self.time_data = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.on_update_clear_clicked)
        self.states_reader = StatesReader()
        self.timer.start(1000)

    def setup_ui(self):
        self.setWindowTitle("StandCO")
        palette = self.palette()
        palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor("#2C3539"))
        self.setPalette(palette)
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(5, 5, 5, 5)

        content_layout = QtWidgets.QVBoxLayout()
        content_layout.setSpacing(5)

        content_layout.addLayout(
            self.setup_line_layout(["PD_1", "PD_2", "PD_3", "PD_4", "PD_5", "PD_6"],
                                   ["DD_1", "DD_2", "DD_3"]))
        content_layout.addLayout(
            self.setup_line_layout(["PD_1.1", "PD_2.1", "PD_3.1", "PD_4.1", "PD_5.1", "PD_6.1"],
                                   ["DD_1.1", "DD_2.1", "DD_3.1"]))
        content_layout.addLayout(
            self.setup_line_layout(["PD_1.2", "PD_2.2", "PD_3.2", "PD_4.2", "PD_5.2", "PD_6.2"],
                                   ["DD_1.2", "DD_2.2", "DD_3.2"]))
        content_layout.addLayout(
            self.setup_line_layout(["PD_1.3", "PD_2.3", "PD_3.3", "PD_4.3", "PD_5.3", "PD_6.3"],
                                   ["DD_1.3", "DD_2.3", "DD_3.3"]))
        content_layout.addLayout(self.test_btn_panel())

        main_layout.addLayout(content_layout)
        main_layout.addLayout(self.setup_status_bar())

        self.setLayout(main_layout)
        self.status_bar.setVisible(False)
        self.state = False

    def setup_status_bar(self):
        status_bar_layout = QtWidgets.QHBoxLayout()
        self.status_bar = QtWidgets.QStatusBar()
        self.status_bar.setSizeGripEnabled(False)
        status_bar_layout.addWidget(self.status_bar)

        return status_bar_layout

    def setup_relays_indicators(self, relays_labels):
        indicators_layout = QtWidgets.QHBoxLayout()
        for i in range(3):
            indicator = RelayIndicator(relays_labels[i])
            var_name = self.remove_dot(relays_labels[i])
            setattr(self, var_name, indicator)
            indicators_layout.addWidget(indicator)
        return indicators_layout

    def setup_plot(self, sensor_name):
        plot_layout = QtWidgets.QHBoxLayout()
        plot = GraphPlot(sensor_name)
        var_name = self.remove_dot(sensor_name)
        setattr(self, var_name, plot)
        plot_layout.addWidget(plot)
        return plot_layout

    def remove_dot(self, name):
        name = name.replace(".", "_")
        return name

    def setup_line_layout(self, relays_labels, sensors_labels):
        line_layout = QtWidgets.QHBoxLayout()
        for i in range(3):
            line_layout.addLayout(self.setup_plot(sensors_labels[i]))
            if relays_labels:
                line_layout.addLayout(self.setup_relays_indicators(relays_labels))
                relays_labels = relays_labels[3:]
        return line_layout

    def test_btn_panel(self):
        panel = QtWidgets.QHBoxLayout()
        self.clear_plot_btn = QtWidgets.QPushButton("Clear")
        self.update_plot_btn = QtWidgets.QPushButton("Update")
        panel.addWidget(self.clear_plot_btn)
        panel.addWidget(self.update_plot_btn)
        self.clear_plot_btn.clicked.connect(self.on_clear_btn_clicked)
        self.update_plot_btn.clicked.connect(self.on_update_clear_clicked)
        return panel

    def on_clear_btn_clicked(self):
        self.DD_1.clear_graph()

    def on_update_clear_clicked(self):
        timestamp = datetime.now().strftime("%H:%M:%S")
        r_data, s_data = self.states_reader.read()
        # self.DD_1.update_data(pressure_value=self.p_data, temperature_value=self.t_data, time_value=self.time_data)
        # self.DD_2_1.update_data(pressure_value=self.p_data, temperature_value=self.t_data,
        #                         time_value=self.time_data)
        # self.DD_3_2.update_data(pressure_value=self.p_data, temperature_value=self.t_data,
        #                         time_value=self.time_data)
        # self.state = not self.state
        # self.RD_1.set_state(self.state)
        # self.RD_2_1.set_state(not self.state)
        # self.p_data += 1
        # self.t_data -= 1
        # self.time_data += 12
        self.update_relays(r_data)
        self.update_sensors(s_data, timestamp)

    def update_sensors(self, s_data, timestamp):
        for value in s_data:
            sensor_name = self.remove_dot(value["name"])
            sensor = getattr(self, sensor_name)
            pressure = round(value["pressure"], 4)
            temperature = round(value["temperature"], 4)
            sensor.update_data(pressure, temperature, timestamp)

    def update_relays(self, r_data):
        for value in r_data:
            relay_name = self.remove_dot(value["name"])
            relay = getattr(self, relay_name)
            if relay:
                if relay.state != value["state"]:
                    relay.set_state(value["state"])
