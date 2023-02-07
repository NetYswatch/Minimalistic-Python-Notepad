
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from MyPackage.modules.window_handler import WindowHandler


class ApplicationHandler():
        
    def main(self) -> None:
        application = QApplication(sys.argv)
        window = QWidget()
        handler = WindowHandler(application, window)
        handler.show_window()

if __name__ == "__main__":
        ApplicationHandler().main()
