from windows.image_detection.window import ImageDetectionWindow
from detection.main import VideoDetection
from supporting.common import decorator_check_folder_path, decorator_check_file_path, decorator_get_parameters


class VideoDetectionWindow(ImageDetectionWindow):
    file_filter = "Videos (*.mp4)"

    @decorator_check_file_path
    @decorator_check_folder_path
    @decorator_get_parameters
    def detect(self):
        VideoDetection(self).detect()
