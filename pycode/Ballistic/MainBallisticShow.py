from PyQt6.QtWidgets import QWidget, QPushButton
from .BallisticFigure import BallisticFigure
from PyQt6 import uic
from PyQt6.QtCore import QTimer, QPointF, QRect
from PyQt6.QtGui import QPainter, QColor, QIcon
import io
from templates_py.main_ballistic_show import main_ballistic_show
from sheets_py.show_window_sheet import show_window_sheet


class MainBallisticShow(QWidget):
    """Класс для визуализации полёта тела
    """
    
    def __init__(self, figure: BallisticFigure, g: float, parent=None):
        super().__init__()
        self.move(100, 100)
        uic.loadUi(io.StringIO(main_ballistic_show), self)
        self.setWindowIcon(QIcon("resources/vampire_bat.png"))
        self.exp = parent

        self.setStyleSheet(show_window_sheet)
        
        self.figure = figure
        self.g = g
        
        self.initUI()
    
    def initUI(self):
        self.key_comboBox.addItems(['Координата X', 'Время'])
        
        self.points = []
        # Для каждого х находим у
        # шаг в 3 нужен для того, чтобы траектория была пунктиром
        for x in range(10, 801, 2):
            y = 600 - int(self.figure.get_y(x, self.g))
            self.points.append((x, y))
            # Прекращаем, если вышли за границу
            if y < 0 or y > 600:
                break
        self.coord = 0
        
        text = f'''<p>Масса: {self.figure.mass}кг</p>
        <p>Скорость: {self.figure.v}м/с</p>
        <p>Угол наклона: {self.figure.corner}°</p>
        <p>Ускорение свободного падения: {self.g}м/с²</p>
        <p>Длина полёта: {self.figure.length(self.g)}м</p>
        <p>Время полёта: {self.figure.main_time(self.g)}с</p>
        <p>Максимальная высота полёта: {self.figure.max_high(self.g)}м</p>
        '''
        self.result_textBrowser.setHtml(text)
        
        self.search_btn.clicked.connect(self.search)
        self.value_spinBox.returnPressed.connect(self.search)
        self.value_spinBox.setMaximum(100000000)
        
        # Задаём Х-координаты тела
        x_points = []
        # тело по Х летит от точки 0 до длины полёта тела
        # длину полёта можно найти с помощью метода length у класса BallisticFigure
        for i in range(0, int(self.figure.length(self.g))):
            for j in range(100 * i, 100 * (i + 1)):
                x_points.append(j / 100)
        y_points = []
        for x in x_points:
            # для каждого Х находим У
            y_points.append(self.figure.get_y(x, self.g))
        # Рисуем
        self.graphic.plot(x_points, y_points, pen='r')
        
        self.draw_widget = Draw(self)
        self.tabWidget.addTab(self.draw_widget, 'Анимация')
    
    def search(self):
        value = self.value_spinBox.value()
        if self.key_comboBox.currentText() == 'Время':
            result = f'''<p>Координата тела в момент времени t = {value}:</p>
            <p>(x({value}), y({value})) = {self.figure.get_coord(self.g, value)}</p>'''
        else:
            result = f'''<p>Зависимость координаты Y от X:</p>
            <p>y({value}) = {self.figure.get_y(value, self.g)}</p>'''
        self.search_textBrowser.setHtml(result)


class Draw(QWidget):
    def __init__(self, parent: MainBallisticShow):
        super().__init__()
        self.main_window = parent
        self.start_btn = QPushButton(self)
        self.start_btn.setGeometry(350, 50, 100, 25)
        self.start_btn.setText('Начать')
        self.start_btn.clicked.connect(self.start_animation)
        self.coord = 0
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
    
    def start_animation(self):
        self.timer.start(50)
        self.coord = 1
    
    def paintEvent(self, a0):
        super().paintEvent(a0)
        
        if not self.coord:
            return
        
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        #  Цвет траектории
        qp.setPen(QColor(*self.main_window.figure.rgb()))
        qp.setBrush(QColor(*self.main_window.figure.rgb()))
        self.draw_traectory(qp)
        self.draw_figure(qp)
        # Завершаем рисование
        qp.end()
        
        self.coord += 1
        self.timer.start(50)
    
    def draw_figure(self, qp: QPainter):
        try:
            x, y = self.main_window.points[self.coord]
        except IndexError:
            return
        if x > 800 or y > 600:
            return
        qp.drawEllipse(x - 25, y - 25, 50, 50)
    
    def draw_traectory(self, qp:QPainter):
        # Рисуем
        qp.drawPoints(*map(lambda x: QPointF(*x), self.main_window.points))