from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
import io
from templates_py.ballistic_graphic import ballistic_graphic
from PyQt6.QtGui import QIcon


class BallisticGraphic(QWidget):
    """ Класс для визуализации графика полёта тела """
    
    def __init__(self, parent):
        super().__init__()
        self.main_window = parent
        uic.loadUi(io.StringIO(ballistic_graphic), self)
        self.setWindowIcon(QIcon("resources/vampire_bat.png"))
        self.initUI()
    
    def initUI(self):
        # Задаём Х-координаты тела
        x_points = []
        # тело по Х летит от точки 0 до длины полёта тела
        # длину полёта можно найти с помощью метода length у класса BallisticFigure
        for i in range(0, int(self.main_window.figure.length(self.main_window.g))):
            for j in range(100 * i, 100 * (i + 1)):
                x_points.append(j / 100)
        y_points = []
        for x in x_points:
            # для каждого Х находим У
            y_points.append(self.main_window.figure.get_y(x, self.main_window.g))
        # Рисуем
        self.graphic.plot(x_points, y_points, pen='r')