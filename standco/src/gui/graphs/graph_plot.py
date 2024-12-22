import pyqtgraph as pg
import numpy as np


class GraphPlot(pg.PlotWidget):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.curve = self.plot()
        self.curve.setPen('black', width=2)
        self.setBackground('#c6c6c6')
        self.setTitle(self.title, color='black')
        self.showGrid(x=True, y=True, alpha=.9)
        # self.setLabel('left', y_label, color='black', **{'font-size': '11pt'})
        self.setLabel('bottom', 'Время', color='black',
                      **{'font-size': '10pt'})
        self.setDownsampling(mode="peak")
        self.setMinimumSize(300, 200)

        self.graph_data_y = np.linspace(0, 0, 10)
        self.graph_data_x = np.linspace(0, 0, 10)
        self.setXRange(-9, 0)
        self.ptr1 = 0

    def clear_plot(self):
        self.graph_data_y = np.linspace(0, 0, 10)
        self.graph_data_x = np.linspace(0, 0, 10)
        self.setXRange(-9, 0)
        self.ptr1 = 0
        self.curve.setData(self.graph_data_x, self.graph_data_y)
        self.curve.setPos(self.ptr1, 0)
