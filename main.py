from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from controller import Controller
from PyQt5.QtCore import QSettings
from windows.settings.resources import CONFIG_FILE_NAME


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    settings = QSettings(CONFIG_FILE_NAME, QSettings.IniFormat)
    app.setApplicationName(settings.value("APP_NAME", "ImageAI", type=str))
    app.setWindowIcon(QIcon(settings.value("ICON", "images/icon.ico", type=str)))
    controller = Controller()
    controller.select_forms("main")
    sys.exit(app.exec_())
