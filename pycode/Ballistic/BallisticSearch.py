from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
import io
from templates_py.ballistic_search import ballistic_search
from sheets_py.search_window_sheet import search_window_sheet
from PyQt6.QtGui import QIcon


class BalisticSearch(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.move(1000, 600)
        self.main_window = parent
        uic.loadUi(io.StringIO(ballistic_search), self)
        self.setWindowIcon(QIcon("resources/vampire_bat.png"))
        self.setStyleSheet(search_window_sheet)
        self.search_btn.clicked.connect(self.search)
        self.value_spinBox.returnPressed.connect(self.search)
        self.value_spinBox.setMaximum(100000000)
    
    def search(self):
        value = self.value_spinBox.value()
        if self.key_comboBox.currentText() == 'Время':
            result = f'''<p>Координата тела в момент времени t = {value}:</p>
            <p>(x({value}), y({value})) = {self.main_window.figure.get_coord(self.main_window.g, value)}</p>'''
        else:
            result = f'''<p>Зависимость координаты Y от X:</p>
            <p>y({value}) = {self.main_window.figure.get_y(value, self.main_window.g)}</p>'''
        self.result_textBrowser.setHtml(result)