from PyQt6 import QtWidgets, QtGui, QtCore
import pyqtgraph as pg
from standco.src.gui.graphs.graph_plot import GraphPlot
from standco.src.gui.indicators.relay_indicator import RelayIndicator


class StandGui(QtWidgets.QWidget):
    def __init__(self):
        # super().__init__()
        super().__init__()
        self.setWindowTitle("StandCO")
        palette = self.palette()
        palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor("lightgray"))
        self.setPalette(palette)
        self.setup_ui()

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

        # content_layout = QtWidgets.QGridLayout()
        content_layout = QtWidgets.QVBoxLayout()
        content_layout.setSpacing(5)
        content_layout.addLayout(self.first_line_setup())
        content_layout.addLayout(self.second_line_setup())
        content_layout.addLayout(self.third_line_setup())
        content_layout.addLayout(self.fourth_line_setup())
        # content_layout.addLayout(self.setup_sensors_plots("ДД1"))
        # content_layout.addLayout(self.setup_relay_indicators("RD"))
        # content_layout.addLayout(self.setup_sensors_plots("ДД2"))
        # content_layout.addLayout(self.setup_sensors_plots("ДД3"))
        # content_layout.addLayout(self.setup_relay_indicators("РД1"), 1, 1)
        # content_layout.addLayout(self.setup_relay_indicators("РД2"), 2, 1)
        # content_layout.addLayout(self.setup_relay_indicators("РД"), 3, 1)
        # content_layout.addLayout(self.setup_sensors_plots("ДД2"), 0, 2, 3, 1)
        # content_layout.addLayout(self.setup_sensors_plots("ДД3"), 0, 4, 3, 1)
        main_layout.addLayout(content_layout)

        self.setLayout(main_layout)

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
        self.RD5_1_indicator = RelayIndicator("RD5.1")
        self.RD6_1_indicator = RelayIndicator("RD6.1")
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

    def setup_sensors_plots(self, sensor_title):
        plots_layout = QtWidgets.QVBoxLayout()
        plots_layout.setSpacing(5)
        setattr(self, f"{sensor_title}_plot", GraphPlot(sensor_title))
        plots_layout.addWidget(getattr(self, f"{sensor_title}_plot"))
        for i in range(1, 4):  # Создание графиков для .1, .2, .3
            plot_name = f"{sensor_title}_{i}_plot"
            setattr(self, plot_name, GraphPlot(f"{sensor_title}.{i}"))
            plots_layout.addWidget(getattr(self, plot_name))
        return plots_layout

    def setup_relay_indicators(self, relay_title):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setSpacing(5)

        for i in range(1, 5):  # Для 4 строк
            horizontal_layout = QtWidgets.QHBoxLayout()
            horizontal_layout.setSpacing(0)
            for j in range(1, 4):  # Для 3 индикаторов в строке
                relay_name = f"{relay_title}{j if i == 1 else f'{i}.{j}'}"
                indicator_name = f"{relay_name}_indicator"
                setattr(self, indicator_name, RelayIndicator(relay_name))
                horizontal_layout.addWidget(getattr(self, indicator_name))
            vertical_layout.addLayout(horizontal_layout)

        return vertical_layout
