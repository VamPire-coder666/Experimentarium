from PyQt6.QtWidgets import QWidget
from templates_py.change_exp_theme_window import change_exp_theme_window
from PyQt6 import uic
import io


class ChangeThemeWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.main_window = parent
        uic.loadUi(io.StringIO(change_exp_theme_window), self)
        self.one_btn.clicked.connect(self.change_one)
        self.many_btn.clicked.connect(self.change_many)
    
    def change_one(self):
        self.main_window.show_type = 'one'
        self.close()

    def change_many(self):
        self.main_window.show_type = 'many'
        self.close()