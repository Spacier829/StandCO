from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPainter, QBrush, QColor, QFontMetrics
from PyQt6.QtCore import QSize, Qt


class RelayIndicator(QLabel):
    def __init__(self, relay_name):
        super().__init__()
        self.setFixedSize(QSize(60, 60))
        self.state = None
        self.relay_name = relay_name

    def set_state(self, state):
        self.state = state
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        font_metrics = QFontMetrics(painter.font())
        text_width = font_metrics.horizontalAdvance(self.relay_name)

        text_x = (self.width() - text_width) // 2
        text_y = 15

        painter.setPen(QColor("white"))
        painter.drawText(text_x, text_y, self.relay_name)

        if self.state is True:
            color = QColor("#28C878")
        elif self.state is False:
            color = QColor("gray")
        else:
            color = QColor("red")

        radius = min(self.width(), self.height() - 25) // 4
        center_x = self.width() // 2
        center_y = (self.height() + 15) // 2

        brush = QBrush(color)
        painter.setBrush(brush)
        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawEllipse(center_x - radius, center_y - radius, radius * 2, radius * 2)

        painter.end()
