from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QWidget, QApplication


class CommonWindow(QWidget):
    def __init__(self, window_size, parent=None, *args):
        QWidget.__init__(self, parent, *args)
        self.setFixedSize(*window_size)
        self.move_central()

    def move_central(self):
        desktop = QApplication.desktop()
        self.move(QPoint((desktop.width() - self.width()) // 2, (desktop.height() - self.height()) // 2))
