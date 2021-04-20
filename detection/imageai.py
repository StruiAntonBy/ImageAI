import cv2

from imageai.Detection import ObjectDetection, VideoObjectDetection
from PyQt5.QtCore import QThread, QSettings
from prettytable import PrettyTable
from supporting.common import check_folder_access
from detection.resources import *
from windows.settings.resources import CONFIG_FILE_NAME, KEY_SAVE_MODEL, MODELS


class Thread(QThread):
    def __init__(self, window, type_file, new_file, output_file):
        QThread.__init__(self)
        self.window, self.type_file, self.new_file, self.output_file = (window, type_file, new_file, output_file)

    def _print_table_txt(self, data):
        if check_folder_access(self.window, self.window.folder):
            with open(self.window.folder + TEXT_FILE, "w") as f:
                table = PrettyTable()
                table.field_names = COLUMN_NAMES
                table.add_rows(data.items())
                print(table, file=f)

    def forFull(self, output_arrays, count_arrays, average_output_count):
        self._print_table_txt(average_output_count)

    def run(self):
        detector = ObjectDetection() if self.type_file == "img" else VideoObjectDetection()

        settings = QSettings(CONFIG_FILE_NAME, QSettings.IniFormat)
        model = settings.value(KEY_SAVE_MODEL, MODELS[0], type=str)

        if model == MODELS[0]:
            detector.setModelTypeAsRetinaNet()
            file = MODEL_RETINA_NET
        elif model == MODELS[1]:
            detector.setModelTypeAsYOLOv3()
            file = MODEL_YOLOv3
        else:
            detector.setModelTypeAsTinyYOLOv3()
            file = MODEL_TINY_YOLOv3

        detector.setModelPath(file)
        detector.loadModel(self.window.detection_speed)

        if self.type_file == "img":
            detections = detector.detectObjectsFromImage(
                input_image=self.new_file,
                output_image_path=self.output_file,
                **self.window.getFunctionArg()
            )

            self._print_table_txt({name: len(list(filter(lambda elem: True if elem["name"] == name else False,
                                    detections))) for name in set([obj["name"] for obj in detections])})

        elif self.type_file == "video":
            detector.detectObjectsFromVideo(input_file_path=self.new_file,
                                            output_file_path=self.output_file,
                                            video_complete_function=self.forFull,
                                            **self.window.getFunctionArg())
        else:
            camera = cv2.VideoCapture(self.window.index)

            detector.detectObjectsFromVideo(camera_input=camera,
                                            output_file_path=self.output_file,
                                            video_complete_function=self.forFull,
                                            **self.window.getFunctionArg())
