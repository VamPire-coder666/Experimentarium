from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon


class MKT_ExpWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setWindowIcon(QIcon("resources/vampire_bat.png"))
        self.main_window = parent
        self.initUI()
    
    def initUI(self):
        pass