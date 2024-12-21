from PyQt6 import QtWidgets, QtGui, QtCore
import pyqtgraph as pg
from standco.src.gui.graphs.graph_plot import GraphPlot
from standco.src.gui.indicators.relay_indicator import RelayIndicator


class Stand_Gui(QtWidgets.QWidget):
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

        content_layout = QtWidgets.QGridLayout()
        content_layout.setSpacing(5)
        content_layout.addLayout(self.setup_sensors_plots("DD1"), 0, 0, 3, 1)
        content_layout.addLayout(self.setup_relay_indicators("РД"), 0, 1, 3, 1)
        content_layout.addLayout(self.setup_sensors_plots("DD2"), 0, 2, 3, 1)
        content_layout.addLayout(self.setup_sensors_plots("DD3"), 0, 4, 3, 1)
        main_layout.addLayout(content_layout)

        self.setLayout(main_layout)

    def setup_sensors_plots(self, sensor_title):
        plots_layout = QtWidgets.QVBoxLayout()
        plots_layout.setSpacing(5)
        setattr(self, f"{sensor_title}_plot", GraphPlot(sensor_title, "T"))
        plots_layout.addWidget(getattr(self, f"{sensor_title}_plot"))
        for i in range(1, 4):  # Создание графиков для .1, .2, .3
            plot_name = f"{sensor_title}_{i}_plot"
            setattr(self, plot_name, GraphPlot(f"{sensor_title}.{i}", "T"))
            plots_layout.addWidget(getattr(self, plot_name))
        return plots_layout

    def setup_relay_indicators(self, relay_title):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setSpacing(5)

        for i in range(1, 5):  # Для 4 строк
            horizontal_layout = QtWidgets.QHBoxLayout()
            horizontal_layout.setSpacing(0)
            for j in range(1, 4):  # Для 3 индикаторов в строке
                relay_name = f"{relay_title}{j if i == 1 else f'.{i}.{j}'}"
                indicator_name = f"{relay_name}_indicator"
                setattr(self, indicator_name, RelayIndicator(relay_name))
                horizontal_layout.addWidget(getattr(self, indicator_name))
            vertical_layout.addLayout(horizontal_layout)

        return vertical_layout
