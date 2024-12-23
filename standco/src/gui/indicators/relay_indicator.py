from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPainter, QBrush, QColor, QFontMetrics
from PyQt6.QtCore import QSize, Qt


class RelayIndicator(QLabel):
    def __init__(self, relay_name):
        super().__init__()
        self.setFixedSize(QSize(60, 60))  # Увеличен размер для текста
        self.state = None
        self.relay_name = relay_name  # Название реле

    def set_state(self, state):
        self.state = state
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Определение размера текста
        font_metrics = QFontMetrics(painter.font())
        text_width = font_metrics.horizontalAdvance(self.relay_name)

        # Расположение текста по центру
        text_x = (self.width() - text_width) // 2
        text_y = 15  # Немного сверху, чтобы текст не перекрывал круг

        # Рисуем текст (имя реле)
        painter.setPen(QColor("white"))
        painter.drawText(text_x, text_y, self.relay_name)  # Отображение имени реле в центре

        # Определение цвета для состояния реле
        if self.state is True:
            color = QColor("#28C878")
        elif self.state is False:
            color = QColor("gray")
        else:
            color = QColor("white")

        # Рисуем круг для состояния реле
        radius = min(self.width(), self.height() - 25) // 4  # Уменьшен радиус круга (заменили 2 на 4)
        center_x = self.width() // 2  # Центр по горизонтали
        center_y = (self.height() + 15) // 2  # Центр по вертикали, с учетом текста

        brush = QBrush(color)
        painter.setBrush(brush)
        painter.setPen(Qt.PenStyle.NoPen)

        # Рисуем круг, используя радиус и центр
        painter.drawEllipse(center_x - radius, center_y - radius, radius * 2, radius * 2)

        painter.end()
