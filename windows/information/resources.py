from PyQt5.QtCore import QSettings
from windows.settings.resources import CONFIG_FILE_NAME

WINDOW_SIZE = (320, 150)

settings = QSettings(CONFIG_FILE_NAME, QSettings.IniFormat)
NAME_LABEL_APP_VERSION = "Версия приложения: " + settings.value("APP_VERSION", "1.0.0", type=str)
NAME_LABEL_IMAGE_AI_VERSION = "Версия ImageAI: " + settings.value("IMAGE_AI_VERSION", "2.1.6", type=str)
NAME_LABEL_INFORMATION_QT = "Данно приложение написанно на фреймворке Qt"
