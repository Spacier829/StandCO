import pyqtgraph as pg
import numpy as np


class GraphPlot(pg.PlotWidget):
    def __init__(self, title):
        super().__init__()

        self.setBackground('#2C3539')
        self.setTitle(title, color='white', size='12pt')
        self.showGrid(x=True, y=True, alpha=0.5)

        self.temperature_axis = pg.ViewBox()
        self.getPlotItem().scene().addItem(self.temperature_axis)
        self.getPlotItem().getAxis('right').linkToView(self.temperature_axis)
        self.temperature_axis.setXLink(self)
        self.temperature_axis.setBackgroundColor("#343837")

        self.getPlotItem().showAxis('right')
        self.getPlotItem().getAxis('right').setPen('white')
        self.getPlotItem().getAxis('right').setLabel('Температура (°C)', color='#1F91DC', **{'font-size': '12pt'})
        self.getPlotItem().getAxis('left').setLabel('Давление (Па)', color='#FA3232', **{'font-size': '12pt'})
        self.getPlotItem().getAxis('bottom').setLabel('Время (с)', color='white', **{'font-size': '10pt'})

        self.pressure_curve = self.plot(pen=pg.mkPen('#FA3232', width=2))
        self.temperature_curve = pg.PlotCurveItem(pen=pg.mkPen('#1F91DC', width=2))
        self.temperature_axis.addItem(self.temperature_curve)

        self.update_views()

        # Данные для графиков
        self.time_data = np.linspace(-10, 0, 10)
        self.pressure_data = np.zeros(10)
        self.temperature_data = np.zeros(10)

        # Синхронизация правого вида с основным
        self.getPlotItem().vb.sigResized.connect(self.update_views)
        self.temperature_axis.sigRangeChangedManually.connect(self.rise_auto_button)
        self.getPlotItem().autoBtn.clicked.connect(self.auto_button_signal)

    def update_views(self):
        self.temperature_axis.setGeometry(self.getPlotItem().vb.sceneBoundingRect())
        self.temperature_axis.linkedViewChanged(self.getPlotItem().vb, self.temperature_axis.XAxis)

    def rise_auto_button(self):
        self.getPlotItem().vb.disableAutoRange()
        self.getPlotItem().showButtons()

    def auto_button_signal(self):
        self.temperature_axis.enableAutoRange()

    def update_data(self, pressure_values, temperature_values):
        self.pressure_data = np.roll(self.pressure_data, -len(pressure_values))
        self.pressure_data[-len(pressure_values):] = pressure_values
        self.pressure_curve.setData(self.time_data, self.pressure_data)

        self.temperature_data = np.roll(self.temperature_data, -len(temperature_values))
        self.temperature_data[-len(temperature_values):] = temperature_values
        self.temperature_curve.setData(self.time_data, self.temperature_data)

    def clear_graph(self):
        """Очистить графики."""
        self.pressure_data.fill(0)
        self.temperature_data.fill(0)
        self.pressure_curve.clear()
        self.temperature_curve.clear()
