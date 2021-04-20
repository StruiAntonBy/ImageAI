import shutil
import os


from PyQt5.QtWidgets import QProgressDialog
from PyQt5.QtCore import Qt, QTimer, QEventLoop
from mutagen.mp4 import MP4
from detection.imageai import Thread
from supporting.common import check_folder_access
from detection.resources import *


class ImageDetection:
    def __init__(self, window):
        self.window = window

    def _start(self, type_file, sleep_time, new_file, output_file):
        progress = QProgressDialog(NAME_PROGRESS_BAR, "", 0, 100, parent=self.window)
        progress.setWindowModality(Qt.WindowModal)
        progress.setCancelButton(None)
        progress.setWindowFlags(progress.windowFlags() & ~Qt.WindowCloseButtonHint)
        progress.setMinimumDuration(0)

        thread = Thread(self.window, type_file, new_file, output_file)
        thread.start()

        while not thread.isFinished() or progress.value() != 99:
            loop = QEventLoop()
            QTimer.singleShot(sleep_time if not thread.isFinished() else 100, loop.quit)
            loop.exec_()
            if progress.value() == 99:
                continue
            progress.setValue(progress.value() + 1)
        progress.cancel()

    def _save(self, output_file):
        if check_folder_access(self.window, self.window.folder):
            shutil.copy(output_file, self.window.folder)

    def _detect(self, type_file, new_file, output_file, sleep_time):
        shutil.copyfile(self.window.file, new_file)

        self._start(type_file, sleep_time, new_file, output_file)

        output_file += "" if type_file == "img" else ".avi"
        self._save(output_file)

        os.remove(new_file)
        os.remove(output_file)

    def detect(self):
        str_end = str(hash(self.window.file)) + "." + self.window.file_format
        self._detect("img", "~f" + str_end, "~d" + str_end, 500)


class VideoDetection(ImageDetection):
    def detect(self):
        str_hash = str(hash(self.window.file))
        self._detect("video", "~f" + str_hash + "." + self.window.file_format, "~d" + str_hash,
                     (MP4(self.window.file).info.length * 120000) / 100 if self.window.file_format == "mp4" else 1000)


class CameraDetection(VideoDetection):
    def __init__(self, window):
        super().__init__(window)

    def _detect(self, type_file, sleep_time):
        output_file = "~d" + str(hash(self.window.file))

        self._start(type_file, sleep_time, None, output_file)

        output_file += ".avi"
        self._save(output_file)

        os.remove(output_file)

    def detect(self):
        self._detect("camera", (self.window.detection_timeout * 120000) / 100)
