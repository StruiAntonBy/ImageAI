from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QLabel, QMessageBox
from supporting.resources import *

import os
import cv2

getValueCheckBox = lambda check_box: False if check_box.checkState() == 0 else True


class ClickedLabel(QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)

        self.clicked.emit()


def check_folder_access(window, folder):
    if not os.path.exists(folder):
        QMessageBox.critical(window, TITLE_MESSAGE_CRITICAL, MESSAGE_ERROR_SPECIFIED_FOLDER_DOES_NOT_EXIST)
        return False
    return True


#  ----------------------decorators--------------------------------

def decorator_modal_window(func):
    def wrapped(self):
        window = func(self)
        window.setWindowModality(Qt.WindowModal)
        window.show()
    return wrapped


def decorator_check_folder_path(func):
    def wrapped(self):
        if not check_folder_access(self, self.folder):
            pass
        elif self.folder == "...":
            QMessageBox.warning(self, TITLE_MESSAGE_WARNING, MESSAGE_WARNING_FOLDER_PATH_IS_NOT_SPECIFIED)
        else:
            func(self)
    return wrapped


def decorator_check_file_path(func):
    def wrapped(self):
        if not os.path.exists(self.file):
            QMessageBox.critical(self, TITLE_MESSAGE_CRITICAL, MESSAGE_ERROR_SPECIFIED_FILE_DOES_NOT_EXIST)
        elif not os.path.isfile(self.file):
            QMessageBox.warning(self, TITLE_MESSAGE_WARNING, MESSAGE_WARNING_FILE_PATH_IS_NOT_SPECIFIED)
        else:
            func(self)
    return wrapped


def decorator_get_parameters(func):
    def wrapped(self):
        self._getParameters()
        func(self)
    return wrapped


def decorator_check_camera(func):
    def wrapped(self):
        capture = cv2.VideoCapture(self.index)
        if capture is None or not capture.isOpened():
            QMessageBox.warning(self, TITLE_MESSAGE_WARNING, MESSAGE_WARNING_UNABLE_OPEN_CAMERA + str(self.index))
        else:
            func(self)
    return wrapped
