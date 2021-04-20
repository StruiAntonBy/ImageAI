from windows.common import CommonWindow
from windows.information.resources import *
from windows.settings.resources import NAME_BTN_BACK
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import pyqtSignal
from supporting.common import ClickedLabel


class InformationWindow(CommonWindow):
    switch_window = pyqtSignal(str)

    def __init__(self, parent=None, *args):
        CommonWindow.__init__(self, WINDOW_SIZE, parent, *args)
        label_image_ai_version = QLabel(NAME_LABEL_IMAGE_AI_VERSION)
        label_app_version = QLabel(NAME_LABEL_APP_VERSION)

        label_information_qt = ClickedLabel(NAME_LABEL_INFORMATION_QT)
        label_information_qt.clicked.connect(lambda: QMessageBox.aboutQt(self))

        btn_back = QPushButton(NAME_BTN_BACK)
        btn_back.clicked.connect(self.back)

        vbox = QVBoxLayout()
        for widget in [label_image_ai_version, label_app_version, label_information_qt, btn_back]:
            vbox.addWidget(widget)

        self.setLayout(vbox)

    def back(self):
        self.switch_window.emit("main<information")
