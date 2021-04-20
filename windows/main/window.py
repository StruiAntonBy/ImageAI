from PyQt5.QtWidgets import QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from windows.common import CommonWindow
from windows.image_detection.window import ImageDetectionWindow
from windows.main.resources import *
from windows.video_detection.window import VideoDetectionWindow
from windows.camera_detection.window import CameraDetectionWindow
from supporting.common import decorator_modal_window


class MainWindow(CommonWindow):
    switch_window = pyqtSignal(str)

    def __init__(self, parent=None):
        CommonWindow.__init__(self, WINDOW_SIZE, parent)

        list_functions = [self.image_detection, self.video_detection, self.camera_detection, self.get_settings,
                          self.get_information]

        vbox = QVBoxLayout()

        for i, name in enumerate(NAME_BUTTONS):
            btn = QPushButton(name)
            btn.clicked.connect(list_functions[i])
            vbox.addWidget(btn)

        self.setLayout(vbox)

    @decorator_modal_window
    def image_detection(self):
        return ImageDetectionWindow(self, Qt.Window)

    @decorator_modal_window
    def video_detection(self):
        return VideoDetectionWindow(self, Qt.Window)

    @decorator_modal_window
    def camera_detection(self):
        return CameraDetectionWindow(self, Qt.Window)

    def get_information(self):
        self.switch_window.emit("main>information")

    def get_settings(self):
        self.switch_window.emit("main>settings")
