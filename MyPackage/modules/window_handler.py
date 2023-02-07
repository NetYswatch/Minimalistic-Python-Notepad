from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QFileDialog, QPlainTextEdit, QTextEdit, QMessageBox
from PyQt5 import Qt
from PyQt5.QtGui import QColor
import sys
from PyQt5 import uic



class WindowHandler():
    def __init__(self, application, window):
        self.application = application
        self.window = window
        self.window = uic.loadUi("MyPackage/UI/MainWindow.ui")
        self.load_button = self.window.findChild(QPushButton, "pushButton")
        self.load_button.clicked.connect(self.load_save)
        self.save_button = self.window.findChild(QPushButton, "SaveFileButton")
        self.save_button.clicked.connect(self.save_file)
        self.text_box = self.window.findChild(QTextEdit, "textEdit")
        self.settings_button = self.window.findChild(QPushButton, "Settings")
        self.settings_button.clicked.connect(self.darkmode_enabler)
        #self.textbox = self.window.findChild(QTextEdit, "textEdit")



    def show_window(self, stay_open=True): 
            """
            Show the window and load the UI found in ../UI
            
            Parameters:
            stay_open (bool): If True, the window will stay open until closed manually.
                            If False, the window will close immediately after being shown.
                            Default is True. (Setting to false will enable tests to be ran on the class)            
            """
            self.window.setFixedSize(697, 452 )
            self.window.setWindowTitle("Shitty Python Notepad")
            self.window.show()

            if stay_open:
                sys.exit(self.application.exec_())
           
    def darkmode_enabler(self):
        self.text_box.setTextColor(QColor(255, 0, 0))
        self.text_box.setStyleSheet("QTextEdit { background-color: rgb(0, 0, 0); }")




    def load_save(self):
            """Custom slot to handle the "Load file" button click."""
            try:

                options = QFileDialog.Options()
                options |= QFileDialog.ReadOnly
                file_name, _ = QFileDialog.getOpenFileName(self.window, "Open file", "", "All Files (*);;Text Files (*.txt)", options=options)
                if file_name:
                    with open(file_name, 'r') as f:
                        file_contents = f.read()
                        self.text_box.setPlainText(file_contents)
            except Exception as e:
                QMessageBox.warning(self.window, "Error", "An error occurred while loading the file.")
                print(e)

                    
                
    def save_file(self):
            try:
                options = QFileDialog.Options()
                options |= QFileDialog.ReadOnly
                file_name, _ = QFileDialog.getSaveFileName(self.window, "Open file", "", "All Files (*);;Text Files (*.txt)", options=options)
                with open(file_name, 'w') as f:
                    f.write(self.text_box.toPlainText())
                
            except (UnicodeEncodeError, Exception) as e:
                QMessageBox.warning(self.window, "Error", "An error occurred while saving the file.")
                print(e)
                

    
     








    
            
