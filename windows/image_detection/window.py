from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QFileDialog, QCheckBox, QComboBox, QSpinBox, QMessageBox
from PyQt5.QtCore import Qt
from windows.image_detection.resources import *
from windows.common import CommonWindow
from detection.main import ImageDetection
from supporting.common import getValueCheckBox, decorator_check_file_path, decorator_check_folder_path,\
    decorator_get_parameters


class ImageDetectionWindow(CommonWindow):
    file_filter, file, folder = "Images (*.jpg *.jpeg)", "...", "...",

    def __init__(self, parent=None, *args):
        CommonWindow.__init__(self, WINDOW_SIZE, parent, *args)
        self.build()
        self.placement(NAME_LABELS)

    def build(self):
        btn_get_file = QPushButton(self.file)
        btn_get_file.clicked.connect(self.get_file)

        btn_get_folder = QPushButton(self.folder)
        btn_get_folder.clicked.connect(self.get_folder)

        combo_box = QComboBox()
        combo_box.addItems(LIST_SPEEDS)

        spin_box_min_percent_probability = QSpinBox()
        spin_box_min_percent_probability.setValue(DEFAULT_MIN_PERCENTAGE_PROBABILITY)

        check_box_percent_probability = QCheckBox()
        check_box_percent_probability.setCheckState(Qt.Unchecked)

        check_box_obj_name = QCheckBox()
        check_box_obj_name.setCheckState(Qt.Unchecked)

        self.btn_detect = QPushButton(NAME_BUTTON)
        self.btn_detect.clicked.connect(self.detect)

        self.widgets = [btn_get_file, btn_get_folder, combo_box, spin_box_min_percent_probability,
                        check_box_percent_probability, check_box_obj_name]

    def placement(self, name_labels):
        grid = QGridLayout()

        for i, widget in enumerate(self.widgets):
            grid.addWidget(QLabel(name_labels[i]), i, 0)
            grid.addWidget(widget, i, 1)
        grid.addWidget(self.btn_detect)

        self.setLayout(grid)

    def get_file(self):
        res = QFileDialog.getOpenFileName(self, filter=self.file_filter)
        if res[0] != "":
            self.file = res[0]
            self.widgets[0].setText(self.file[:10] + "...")
            QMessageBox.information(self, TITLE_MESSAGE_INFORMATION, MESSAGE_INFORMATION_SET_PATH.format(self.file))

    def get_folder(self):
        res = QFileDialog.getExistingDirectory(self)
        if res != "":
            self.folder = res
            self.widgets[1].setText(self.folder[:10] + "...")
            QMessageBox.information(self, TITLE_MESSAGE_INFORMATION, MESSAGE_INFORMATION_SET_PATH.format(self.folder))

    def getFunctionArg(self):
        return {
            "minimum_percentage_probability": self.minimum_percentage_probability,
            "display_percentage_probability": self.display_percentage_probability,
            "display_object_name": self.display_object_name,
        }

    def _getParameters(self):
        self.detection_speed = self.widgets[2].currentText()
        self.minimum_percentage_probability = self.widgets[3].value()
        self.display_percentage_probability = not getValueCheckBox(self.widgets[4])
        self.display_object_name = not getValueCheckBox(self.widgets[5])
        self.file_format = self.file.split(".").pop()

    @decorator_check_file_path
    @decorator_check_folder_path
    @decorator_get_parameters
    def detect(self):
        ImageDetection(self).detect()
