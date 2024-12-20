from PyQt6 import QtWidgets, QtGui, QtCore
import pyqtgraph as pg
from standco.src.gui.graphs.graph_plot import GraphPlot


class Stand_Gui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StandCO")
        self.setup_ui()

    def setup_ui(self):
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(5, 5, 5, 5)

        content_layout = QtWidgets.QGridLayout()
        content_layout.setSpacing(5)
        content_layout.addLayout(self.setup_plots_DD("DD1"), 0, 0, 3, 1)
        content_layout.addLayout(self.setup_plots_DD("DD2"), 0, 3, 3, 1)
        content_layout.addLayout(self.setup_plots_DD("DD3"), 0, 5, 3, 1)
        main_layout.addLayout(content_layout)

        self.setLayout(main_layout)

    def setup_plots_DD(self, title):
        plots_layout = QtWidgets.QVBoxLayout()
        plots_layout.setSpacing(5)
        self.DD_plot = GraphPlot(title, "T")
        plots_layout.addWidget(self.DD_plot)
        self.DD1_plot = GraphPlot(title + ".1", "T")
        plots_layout.addWidget(self.DD1_plot)
        self.DD2_plot = GraphPlot(title + ".2", "T")
        plots_layout.addWidget(self.DD2_plot)
        self.DD3_plot = GraphPlot(title + ".3", "T")
        plots_layout.addWidget(self.DD3_plot)
        return plots_layout
