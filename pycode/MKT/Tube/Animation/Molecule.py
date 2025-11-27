from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPen, QPainter


class Molecule:
    """ Класс молекулы для движения в трубе """
    
    def __init__(self, x, y, radius, color, delta_x, delta_y):
        # координаты молекулы
        self.x = x
        self.y = y
        self.radius = radius # радиус
        self.color = color # цвет
        self.delta_x = delta_x 
        self.delta_y = delta_y
    
    def move(self, width: int, height: int):
        """ Функция для перемещения молекулы
        (изменяет координаты)

        Args:
            width (int): длина, за которую нельзя заходить
            height (int): ширина, за которую нельзя заходить
        """
        
        # Двигаем молекулу
        self.x += self.delta_x
        self.y += self.delta_y
        
        # Проверяем столкновение с левой и правой стенками
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.delta_x = -self.delta_x
        elif self.x + self.radius >= width:
            self.x = width - self.radius
            self.delta_x = -self.delta_x
        
        # Проверяем столкновение с верхней и нижней стенками
        if self.y - self.radius <= 0:
            self.y = self.radius
            self.delta_y = -self.delta_y
        elif self.y + self.radius >= height:
            self.y = height - self.radius
            self.delta_y = -self.delta_y
    
    def draw(self, qp: QPainter):
        """ Функция для отрисовки молекулы

        Args:
            qp (QPainter): QPainter, которым надо нарисовать
        """
        
        # Рисуем
        qp.setBrush(self.color)
        qp.setPen(QPen(Qt.GlobalColor.black, 1))
        qp.drawEllipse(QPointF(self.x, self.y), self.radius, self.radius)

