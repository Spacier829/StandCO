from PyQt6 import QtWidgets, QtGui, QtCore
from standco.src.gui.graphs.graph_plot import GraphPlot
from standco.src.gui.indicators.relay_indicator import RelayIndicator
from standco.src.states_reader.states_reader import StatesReader
from datetime import datetime


class StandGui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.states_reader = StatesReader()
        self.plot_counter = 0
        self.plots = []
        self.sensors_names = []
        self.relays_names = []
        self.setup_ui()
        self.timer = QtCore.QTimer()

    def setup_ui(self):
        self.setWindowTitle("StandCO")
        palette = self.palette()
        palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor("#2C3539"))
        self.setPalette(palette)
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(5, 5, 5, 5)

        content_layout = QtWidgets.QVBoxLayout()
        content_layout.setSpacing(0)

        content_layout.addLayout(self.setup_plot(["DD_1", "DD_1.1", "DD_1.2", "DD_1.3"]))
        content_layout.addLayout(self.setup_plot(["DD_2", "DD_2.1", "DD_2.2", "DD_2.3"]))
        content_layout.addLayout(self.setup_plot(["DD_3", "DD_3.1", "DD_3.2", "DD_3.3"]))
        content_layout.addLayout(self.setup_relays_indicators(["PD_1", "PD_2", "PD_3", "PD_4", "PD_5", "PD_6"]))
        content_layout.addLayout(
            self.setup_relays_indicators(["PD_1.1", "PD_2.1", "PD_3.1", "PD_4.1", "PD_5.1", "PD_6.1"]))
        content_layout.addLayout(
            self.setup_relays_indicators(["PD_1.2", "PD_2.2", "PD_3.2", "PD_4.2", "PD_5.2", "PD_6.2"]))
        content_layout.addLayout(
            self.setup_relays_indicators(["PD_1.3", "PD_2.3", "PD_3.3", "PD_4.3", "PD_5.3", "PD_6.3"]))


        main_layout.addLayout(content_layout)
        main_layout.addLayout(self.control_panel())
        main_layout.addLayout(self.setup_status_bar())

        self.setLayout(main_layout)

    def setup_status_bar(self):
        status_bar_layout = QtWidgets.QHBoxLayout()
        self.status_bar = QtWidgets.QStatusBar()
        self.status_bar.setSizeGripEnabled(False)
        status_bar_layout.addWidget(self.status_bar)
        self.status_bar.setVisible(False)

        return status_bar_layout

    def setup_relays_indicators(self, relays_labels):
        indicators_layout = QtWidgets.QHBoxLayout()
        for i in range(6):
            indicator = RelayIndicator(relays_labels[i])
            var_name = self.remove_dot(relays_labels[i])
            setattr(self, var_name, indicator)
            self.relays_names.append(var_name)
            indicators_layout.addWidget(indicator)
        return indicators_layout

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

    def control_panel(self):
        panel = QtWidgets.QHBoxLayout()
        self.clear_btn = QtWidgets.QPushButton("Остановить")
        self.update_btn = QtWidgets.QPushButton("Начать чтение")
        panel.addWidget(self.clear_btn)
        panel.addWidget(self.update_btn)
        self.clear_btn.clicked.connect(self.on_clear_btn_clicked)
        self.update_btn.clicked.connect(self.on_update_btn_clicked)
        self.clear_btn.setEnabled(False)
        return panel

    def on_clear_btn_clicked(self):
        self.clear_btn.setEnabled(False)
        self.update_btn.setEnabled(True)
        self.timer.stop()
        self.clear()

    def on_update_btn_clicked(self):
        self.update_btn.setEnabled(False)
        self.clear_btn.setEnabled(True)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)

    def update_relays(self, r_data):
        for value in r_data:
            relay_name = self.remove_dot(value["name"])
            relay = getattr(self, relay_name)
            if relay:
                if relay.state != value["state"]:
                    relay.set_state(value["state"])

    # Под рефакторинг
    def setup_plot(self, sensors_labels):
        plot_layout = QtWidgets.QHBoxLayout()
        self.plot_counter += 1
        plot = GraphPlot(sensors_labels)
        setattr(self, f'plot_{self.plot_counter}', plot)
        self.plots.append(getattr(self, f'plot_{self.plot_counter}'))
        plot_layout.addWidget(plot)
        return plot_layout

    def update_data(self):
        r_data, s_data = self.states_reader.read()

        # self.update_relays(r_data)
        self.update_sensors(s_data)

    # Под рефакторинг
    def update_sensors(self, s_data):
        for plot in self.plots:
            plot.update_data(s_data)

    # Под рефакторинг
    def clear(self):

        for sensor in self.sensors_names:
            plot = getattr(self, sensor)
            plot.clear_graph()
        for relay in self.relays_names:
            indicator = getattr(self, relay)
            indicator.set_state(False)

    def closeEvent(self, event):
        self.timer.stop()
        self.states_reader.close_util()
        event.accept()
