from PyQt5.QtWidgets import QGridLayout, QPushButton, QComboBox, QLabel
from PyQt5.QtCore import pyqtSignal, QSettings
from windows.common import CommonWindow
from windows.settings.resources import *


class SettingsWindow(CommonWindow):
    switch_window = pyqtSignal(str)

    def __init__(self, parent=None):
        CommonWindow.__init__(self, WINDOW_SIZE, parent)

        self.combo_box = QComboBox()
        self.combo_box.addItems(MODELS)
        self.combo_box.activated[str].connect(self.onChanged)

        btn_back = QPushButton(NAME_BTN_BACK)
        btn_back.clicked.connect(self.back)

        grid = QGridLayout()
        grid.addWidget(QLabel(NAME_LABEL), 0, 0)
        grid.addWidget(self.combo_box, 0, 1)
        grid.addWidget(btn_back)

        self.setLayout(grid)

        self.combo_box.setCurrentText(QSettings(CONFIG_FILE_NAME, QSettings.IniFormat).value(KEY_SAVE_MODEL, MODELS[0],
                                    type=str))

    def onChanged(self):
        QSettings(CONFIG_FILE_NAME, QSettings.IniFormat).setValue(KEY_SAVE_MODEL, self.combo_box.currentText())

    def back(self):
        self.switch_window.emit("main<settings")
