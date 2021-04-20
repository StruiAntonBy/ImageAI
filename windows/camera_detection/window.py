from windows.video_detection.window import VideoDetectionWindow
from detection.main import CameraDetection
from supporting.common import getValueCheckBox, decorator_check_folder_path, decorator_get_parameters,\
    decorator_check_camera
from PyQt5.QtWidgets import QSpinBox
from windows.common import CommonWindow
from windows.camera_detection.resources import *


class CameraDetectionWindow(VideoDetectionWindow):
    file = None

    def __init__(self, parent=None, *args):
        CommonWindow.__init__(self, WINDOW_SIZE, parent, *args)
        self.build()
        self.placement(NAME_LABELS)

    def get_file(self):
        raise AttributeError("'{0}' object has no attribute 'get_file'".format(self.__name__))

    def build(self):
        super().build()
        self.widgets[0] = QSpinBox()

        for i, widget in enumerate([SPIN_BOX_FRAMES_PER_SECOND, SPIN_BOX_DETECTION_TIMEOUT], 3):
            spin_box = QSpinBox()
            spin_box.setRange(*widget["Range"])
            spin_box.setValue(widget["Default"])
            self.widgets.insert(i, spin_box)

    def _getParameters(self):
        self.index = self.widgets[0].value()
        self.detection_speed = self.widgets[2].currentText()
        self.frames_per_second = self.widgets[3].value()
        self.detection_timeout = self.widgets[4].value()
        self.minimum_percentage_probability = self.widgets[5].value()
        self.display_percentage_probability = not getValueCheckBox(self.widgets[6])
        self.display_object_name = not getValueCheckBox(self.widgets[7])

    def getFunctionArg(self):
        d = super().getFunctionArg()
        d["frames_per_second"] = self.frames_per_second
        d["detection_timeout"] = self.detection_timeout
        return d

    @decorator_check_folder_path
    @decorator_get_parameters
    @decorator_check_camera
    def detect(self):
        CameraDetection(self).detect()
