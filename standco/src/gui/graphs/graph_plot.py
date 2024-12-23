import pyqtgraph as pg
import numpy as np


class GraphPlot(pg.PlotWidget):
    def __init__(self, title="График с двумя осями"):
        super().__init__()

        # Настройки основного графика
        self.setBackground('#c6c6c6')
        self.setTitle(title, color='black', size='12pt')
        self.showGrid(x=True, y=True, alpha=0.8)

        # Левая ось Y — давление
        self.setLabel('left', 'Давление (Па)', color='blue', **{'font-size': '10pt'})
        self.left_curve = self.plot(pen=pg.mkPen('blue', width=2))  # Кривая давления

        # Нижняя ось X — время
        self.setLabel('bottom', 'Время (с)', color='black', **{'font-size': '10pt'})

        # Правая ось Y — температура
        self.right_axis = pg.ViewBox()  # Дополнительный вид для правой оси
        self.getPlotItem().scene().addItem(self.right_axis)  # Добавляем вид в сцену
        self.getPlotItem().getAxis('right').linkToView(self.right_axis)  # Связываем оси
        self.right_axis.setXLink(self)  # Связь осей X

        # Настройки правой оси
        self.getPlotItem().showAxis('right')  # Включение правой оси
        self.getPlotItem().getAxis('right').setPen('red')  # Цвет оси
        self.getPlotItem().getAxis('right').setLabel('Температура (°C)', color='red', **{'font-size': '10pt'})

        # Кривая температуры
        self.right_curve = pg.PlotCurveItem(pen=pg.mkPen('red', width=2))
        self.right_axis.addItem(self.right_curve)

        # Синхронизация правого вида с основным
        self.getPlotItem().vb.sigResized.connect(self.update_views)

        # Данные для графиков
        self.time_data = np.linspace(-10, 0, 100)
        self.pressure_data = np.zeros(100)
        self.temperature_data = np.zeros(100)

    def update_views(self):
        """Синхронизировать правую ось с основной."""
        self.right_axis.setGeometry(self.getPlotItem().vb.sceneBoundingRect())
        self.right_axis.linkedViewChanged(self.getPlotItem().vb, self.right_axis.XAxis)

    def update_data(self, pressure_values, temperature_values):
        """Обновить данные графиков."""
        self.pressure_data = np.roll(self.pressure_data, -len(pressure_values))
        self.pressure_data[-len(pressure_values):] = pressure_values
        self.left_curve.setData(self.time_data, self.pressure_data)

        self.temperature_data = np.roll(self.temperature_data, -len(temperature_values))
        self.temperature_data[-len(temperature_values):] = temperature_values
        self.right_curve.setData(self.time_data, self.temperature_data)

    def clear_graph(self):
        """Очистить графики."""
        self.pressure_data.fill(0)
        self.temperature_data.fill(0)
        self.left_curve.clear()
        self.right_curve.clear()