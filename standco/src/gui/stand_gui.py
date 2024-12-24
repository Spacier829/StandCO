from PyQt6 import QtWidgets, QtGui, QtCore
import pyqtgraph as pg
from standco.src.gui.graphs.graph_plot import GraphPlot
from standco.src.gui.indicators.relay_indicator import RelayIndicator


class StandGui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StandCO")
        palette = self.palette()
        palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor("#2C3539"))
        self.setPalette(palette)
        self.setup_ui()
        self.p_data = 1
        self.t_data = -1
        self.time_data = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.on_update_clear_clicked)
        # self.timer.start(1000)
        # layout = QtWidgets.QVBoxLayout(self)
        #
        # self.indicator1 = RelayIndicator("РД1")
        # self.indicator2 = RelayIndicator("РД1.1")
        # self.indicator3 = RelayIndicator("РД1.2")
        #
        # layout.addWidget(self.indicator1)
        # layout.addWidget(self.indicator2)
        # layout.addWidget(self.indicator3)
        #
        # # Пример установки состояний
        # self.indicator1.set_state(True)  # Зеленый
        # self.indicator2.set_state(False)  # Серый

    def setup_ui(self):
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(5, 5, 5, 5)

        content_layout = QtWidgets.QVBoxLayout()
        content_layout.setSpacing(5)

        # content_layout.addLayout(self.setup_plot())
        # content_layout.addLayout(self.test_btn_panel())
        # content_layout.addLayout(self.first_line_setup())
        # content_layout.addLayout(self.second_line_setup())
        # content_layout.addLayout(self.third_line_setup())
        # content_layout.addLayout(self.fourth_line_setup())
        content_layout.addLayout(self.setup_line_layout())

        main_layout.addLayout(content_layout)

        self.setLayout(main_layout)

    def setup_relays_indicators(self, relays_labels):
        indicators_layout = QtWidgets.QHBoxLayout()
        for i in range(3):
            indicator = RelayIndicator(relays_labels[i])
            var_name = self.translit_name(relays_labels[i])
            setattr(self, var_name, indicator)
            indicators_layout.addWidget(indicator)
        return indicators_layout

    def setup_plot(self, sensor_name):
        plot_layout = QtWidgets.QHBoxLayout()
        plot = GraphPlot(sensor_name)
        var_name = self.translit_name(sensor_name)
        setattr(self, var_name, plot)
        plot_layout.addWidget(plot)
        return plot_layout

    def translit_name(self, name):
        name = name.replace(".", "_").replace("Р", "R").replace("Д", "D")
        return name

    def setup_line_layout(self):
        line_layout = QtWidgets.QHBoxLayout()
        first_indicators_labels = ["РД_1", "РД_2", "РД_3", "РД_4", "РД_5", "РД_6"]
        first_sensors_labels = ["ДД_1", "ДД_2", "ДД_3"]
        line_layout.addLayout(self.setup_plot(first_sensors_labels[0]))
        line_layout.addLayout(self.setup_relays_indicators(first_indicators_labels))
        first_indicators_labels = first_indicators_labels[3:]
        line_layout.addLayout(self.setup_plot(first_sensors_labels[1]))
        line_layout.addLayout(self.setup_relays_indicators(first_indicators_labels))
        line_layout.addLayout(self.setup_plot(first_sensors_labels[2]))
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
        self.DD1_plot.clear_graph()

    def on_update_clear_clicked(self):
        self.DD1_plot.update_data(pressure_value=self.p_data, temperature_value=self.t_data, time_value=self.time_data)
        self.DD2_1_plot.update_data(pressure_value=self.p_data, temperature_value=self.t_data,
                                    time_value=self.time_data)
        self.DD3_2_plot.update_data(pressure_value=self.p_data, temperature_value=self.t_data,
                                    time_value=self.time_data)
        self.p_data += 1
        self.t_data -= 1
        self.time_data += 12

    def first_line_setup(self):
        first_line = QtWidgets.QHBoxLayout()
        first_line.setSpacing(5)
        self.DD1_plot = GraphPlot("DD1")
        first_line.addWidget(self.DD1_plot)
        self.RD1_indicator = RelayIndicator("RD1")
        self.RD2_indicator = RelayIndicator("RD2")
        self.RD3_indicator = RelayIndicator("RD3")
        first_line.addWidget(self.RD1_indicator)
        first_line.addWidget(self.RD2_indicator)
        first_line.addWidget(self.RD3_indicator)
        self.DD2_plot = GraphPlot("DD2")
        first_line.addWidget(self.DD2_plot)
        self.RD4_indicator = RelayIndicator("RD4")
        self.RD5_indicator = RelayIndicator("RD5")
        self.RD6_indicator = RelayIndicator("RD6")
        first_line.addWidget(self.RD4_indicator)
        first_line.addWidget(self.RD5_indicator)
        first_line.addWidget(self.RD6_indicator)
        self.DD3_plot = GraphPlot("DD3")
        first_line.addWidget(self.DD3_plot)
        return first_line

    def second_line_setup(self):
        second_line = QtWidgets.QHBoxLayout()
        second_line.setSpacing(5)
        self.DD1_1_plot = GraphPlot("DD1.1")
        second_line.addWidget(self.DD1_1_plot)
        self.RD1_1_indicator = RelayIndicator("RD1.1")
        self.RD2_1_indicator = RelayIndicator("RD2.1")
        self.RD3_1_indicator = RelayIndicator("RD3.1")
        second_line.addWidget(self.RD1_1_indicator)
        second_line.addWidget(self.RD2_1_indicator)
        second_line.addWidget(self.RD3_1_indicator)
        self.DD2_1_plot = GraphPlot("DD2.1")
        second_line.addWidget(self.DD2_1_plot)
        self.RD4_1_indicator = RelayIndicator("RD4.1")
        self.RD4_1_indicator.set_state(False)
        self.RD5_1_indicator = RelayIndicator("RD5.1")
        self.RD6_1_indicator = RelayIndicator("RD6.1")
        self.RD6_1_indicator.set_state(True)
        second_line.addWidget(self.RD4_1_indicator)
        second_line.addWidget(self.RD5_1_indicator)
        second_line.addWidget(self.RD6_1_indicator)
        self.DD3_1_plot = GraphPlot("DD3.1")
        second_line.addWidget(self.DD3_1_plot)
        return second_line

    def third_line_setup(self):
        third_line = QtWidgets.QHBoxLayout()
        third_line.setSpacing(5)
        self.DD1_2_plot = GraphPlot("DD1.2")
        third_line.addWidget(self.DD1_2_plot)
        self.RD1_2_indicator = RelayIndicator("RD1.2")
        self.RD2_2_indicator = RelayIndicator("RD2.2")
        self.RD3_2_indicator = RelayIndicator("RD3.2")
        third_line.addWidget(self.RD1_2_indicator)
        third_line.addWidget(self.RD2_2_indicator)
        third_line.addWidget(self.RD3_2_indicator)
        self.DD2_2_plot = GraphPlot("DD2.2")
        third_line.addWidget(self.DD2_2_plot)
        self.RD4_2_indicator = RelayIndicator("RD4.2")
        self.RD5_2_indicator = RelayIndicator("RD5.2")
        self.RD6_2_indicator = RelayIndicator("RD6.2")
        third_line.addWidget(self.RD4_2_indicator)
        third_line.addWidget(self.RD5_2_indicator)
        third_line.addWidget(self.RD6_2_indicator)
        self.DD3_2_plot = GraphPlot("DD3.2")
        third_line.addWidget(self.DD3_2_plot)
        return third_line

    def fourth_line_setup(self):
        fourth_line = QtWidgets.QHBoxLayout()
        fourth_line.setSpacing(5)
        self.DD1_3_plot = GraphPlot("DD1.3")
        fourth_line.addWidget(self.DD1_3_plot)
        self.RD1_3_indicator = RelayIndicator("RD1.3")
        self.RD2_3_indicator = RelayIndicator("RD2.3")
        self.RD3_3_indicator = RelayIndicator("RD3.3")
        fourth_line.addWidget(self.RD1_3_indicator)
        fourth_line.addWidget(self.RD2_3_indicator)
        fourth_line.addWidget(self.RD3_3_indicator)
        self.DD2_3_plot = GraphPlot("DD2.3")
        fourth_line.addWidget(self.DD2_3_plot)
        self.RD4_3_indicator = RelayIndicator("RD4.3")
        self.RD5_3_indicator = RelayIndicator("RD5.3")
        self.RD6_3_indicator = RelayIndicator("RD6.3")
        fourth_line.addWidget(self.RD4_3_indicator)
        fourth_line.addWidget(self.RD5_3_indicator)
        fourth_line.addWidget(self.RD6_3_indicator)
        self.DD3_3_plot = GraphPlot("DD3.3")
        fourth_line.addWidget(self.DD3_3_plot)
        return fourth_line
