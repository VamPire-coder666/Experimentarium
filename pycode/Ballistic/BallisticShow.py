from PyQt6.QtWidgets import QWidget
from .BallisticFigure import BallisticFigure
from PyQt6 import uic
from PyQt6.QtCore import QTimer, QPointF
from PyQt6.QtGui import QPainter, QColor, QIcon
from .BallisticResult import BallisticResult
from .BallisticSearch import BalisticSearch
from .BallisticGraphic import BallisticGraphic
from templates_py.ballistic_show_window import ballistic_show_window
import io


class BallisticShow(QWidget):
    """Класс для визуализации полёта тела
    """
    
    def __init__(self, figure: BallisticFigure, g: float, parent=None):
        super().__init__()
        self.move(100, 100)
        uic.loadUi(io.StringIO(ballistic_show_window), self)
        self.setWindowIcon(QIcon("resources/vampire_bat.png"))
        self.exp = parent
        
        self.figure = figure
        self.g = g
        self.initUI()
    
    def initUI(self):
        self.points = []
        # Для каждого х находим у
        # шаг в 3 нужен для того, чтобы траектория была пунктиром
        for x in range(0, 801, 3):
            y = 600 - int(self.figure.get_y(x, self.g))
            self.points.append((x, y))
            # Прекращаем, если вышли за границу
            if y < 0 or y > 600:
                break
        self.coord = 0
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(75)
        
        self.frame.hide()
        
        self.windows = {
            'result': BallisticResult(self),
            'search': BalisticSearch(self),
            'graphic': BallisticGraphic(self)
        }
        for key in self.windows.keys():
            self.windows[key].show()
    
    def close(self):
        for key in self.windows.keys():
            self.windows[key].close()
        super().close()

    def paintEvent(self, a0):
        super().paintEvent(a0)
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        #  Цвет траектории
        qp.setPen(QColor(*self.figure.rgb()))
        qp.setBrush(QColor(*self.figure.rgb()))
        self.draw_traectory(qp)
        self.draw_figure(qp)
        # Завершаем рисование
        qp.end()

        self.coord += 1
        self.timer.start(50)
    
    def draw_figure(self, qp: QPainter):
        try:
            x, y = self.points[self.coord]
            if x > 800 or y > 600:
                return
            qp.drawEllipse(x - 25, y - 25, 50, 50)
        except:
            return
    
    def draw_traectory(self, qp:QPainter):
        # Рисуем
        qp.drawPoints(*map(lambda x: QPointF(*x), self.points))