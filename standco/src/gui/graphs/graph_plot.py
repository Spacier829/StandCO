import pyqtgraph as pg
import numpy as np


class GraphPlot(pg.PlotWidget):
    def __init__(self, sensors_labels):
        super().__init__()

        self.setBackground('#2C3539')
        self.showGrid(x=True, y=True, alpha=0.5)

        self.temperature_axis = pg.ViewBox()
        self.getPlotItem().scene().addItem(self.temperature_axis)
        self.getPlotItem().getAxis('right').linkToView(self.temperature_axis)
        self.temperature_axis.setXLink(self)
        self.temperature_axis.setBackgroundColor("#343837")
        self.temperature_axis.setYRange(0, 40)
        self.setYRange(0, 100)

        self.enableAutoRange(axis=pg.ViewBox.YAxis, enable=False)
        self.enableAutoRange(axis=self.temperature_axis.YAxis, enable=False)
        self.getPlotItem().getViewBox().setMouseEnabled(x=False, y=False)
        self.temperature_axis.setMouseEnabled(x=False, y=False)
        self.getPlotItem().hideButtons()
        self.setXRange(-20, 0)

        self.getPlotItem().showAxis('right')
        self.getPlotItem().getAxis('right').setPen('white')
        self.getPlotItem().getAxis('right').setLabel('Температура, °C', color='#1F91DC', **{'font-size': '12pt'})
        self.getPlotItem().getAxis('left').setLabel('Давление, Атм', color='#FA3232', **{'font-size': '12pt'})

        colors = ['#FA3232', '#0000FF', '#1F91DC', '#FFFF00']
        for i in range(len(sensors_labels)):
            pressure_curve = self.plot(pen=pg.mkPen(colors[i], width=2))
            temperature_curve = pg.PlotCurveItem(pen=pg.mkPen(colors[i], width=2))
            name = self.remove_dot(sensors_labels[i])
            setattr(self, f'pressure_curve_{name}', pressure_curve)
            setattr(self, f'temperature_curve_{name}', temperature_curve)
            pressure_data = np.zeros(20)
            temperature_data = np.zeros(20)
            setattr(self, f'pressure_data_{name}', pressure_data)
            setattr(self, f'temperature_data_{name}', temperature_data)
            plot = getattr(self, f'temperature_curve_{name}')
            self.temperature_axis.addItem(plot)

        self.update_views()

        self.pressure_data = np.zeros(20)
        self.temperature_data = np.zeros(20)

        self.getPlotItem().vb.sigResized.connect(self.update_views)

    def update_views(self):
        self.temperature_axis.setGeometry(self.getPlotItem().vb.sceneBoundingRect())
        self.temperature_axis.linkedViewChanged(self.getPlotItem().vb, self.temperature_axis.XAxis)

    def update_data(self, values):
        for value in values:
            name = self.remove_dot(value['name'])
            pressure = getattr(self, f'pressure_data_{name}')
            pressure[:-1] = pressure[1:]
            pressure[-1] = round(value["pressure"], 3)

            temperature = getattr(self, f'temperature_data_{name}')
            temperature[:-1] = temperature[1:]
            temperature[-1] = round(value["temperature"], 3)

            x_range = np.linspace(-20, 0, len(pressure))
            pressure_curve = getattr(self, f'pressure_curve_{name}')
            temperature_curve = getattr(self, f'temperature_curve_{name}')
            pressure_curve.setData(x_range, pressure)
            temperature_curve.setData(x_range, temperature)

    def clear_graph(self):
        self.pressure_data.fill(0)

        self.temperature_data.fill(0)
        self.pressure_curve.clear()
        self.temperature_curve.clear()

    # Добавить штуку для рефакторинга имени графика
    def remove_dot(self, name):
        name = name.replace(".", "_")
        return name
