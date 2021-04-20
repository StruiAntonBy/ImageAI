from windows.main.window import MainWindow
from windows.settings.window import SettingsWindow
from windows.information.window import InformationWindow


class Controller:
    def __init__(self):
        pass

    def select_forms(self, text):
        if text == "main":
            self.main_window = self.start_window(MainWindow)

        if text == "main>settings":
            self.settings = self.go_another_window(SettingsWindow, self.main_window)

        if text == "main<settings":
            self.main_window = self.go_another_window(MainWindow, self.settings)

        if text == "main>information":
            self.information = self.go_another_window(InformationWindow, self.main_window)

        if text == "main<information":
            self.main_window = self.go_another_window(MainWindow, self.information)

    def start_window(self, class_window):
        window = class_window()
        window.switch_window.connect(self.select_forms)
        window.show()
        return window

    def go_another_window(self, class_window, old_window):
        window = self.start_window(class_window)
        old_window.close()
        return window
