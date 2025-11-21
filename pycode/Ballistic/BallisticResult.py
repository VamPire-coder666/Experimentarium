from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
import io
from PyQt6.QtGui import QIcon
from templates_py.ballistic_result import ballistic_result


class BallisticResult(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.move(1000, 100)
        self.main_window = parent
        self.setStyleSheet('background-color: rgb(0, 0, 0)')
        uic.loadUi(io.StringIO(ballistic_result), self)
        self.setWindowIcon(QIcon("resources/vampire_bat.png"))
        text = f'''<p>Масса: {self.main_window.figure.mass}кг</p>
        <p>Скорость: {self.main_window.figure.v}м/с</p>
        <p>Угол наклона: {self.main_window.figure.corner}°</p>
        <p>Ускорение свободного падения: {self.main_window.g}м/с²</p>
        <p>Длина полёта: {self.main_window.figure.length(self.main_window.g)}м</p>
        <p>Время полёта: {self.main_window.figure.main_time(self.main_window.g)}с</p>
        <p>Максимальная высота полёта: {self.main_window.figure.max_high(self.main_window.g)}м</p>
        '''
        self.main_textBrowser.setHtml(text)
        style = '''
        QTextBrowser {
            background-color: #2a3943;
            color: #a9b7c6;
            border: 1px solid #555;
            border-radius: 5px;
            padding: 5px 10px;
            font-family: "monaco", monospace;
        }
        '''
        self.main_textBrowser.setStyleSheet(style)