from PyQt6.QtWidgets import QWidget
try:
    from .Molecule import Molecule
except ImportError:
    from Molecule import Molecule
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QTimer
import random


class Tube(QWidget):
    def __init__(self, parent):
        super().__init__()
        
        self.main_window = parent
        self.molecules = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_balls)
        self.timer.start(150)
        
        self.setStyleSheet('background-color: "black";')
        
        self.create_molecules(self.main_window.T_Slider.value())
    
    def create_molecules(self, T):
        avg_V = round(self.main_window.gas.get_avgV(T)) % 100
        for _ in range(500):
            radius = 5
            x = random.randint(radius, self.width() - radius)
            y = random.randint(radius, self.height() - radius)
            color = QColor(128, 128, 128)
            
            delta_x = random.randint(avg_V - 3, avg_V + 3) * random.choice([1, -1])
            delta_y = random.randint(avg_V - 3, avg_V + 3) * random.choice([1, -1])
            
            self.molecules.append(Molecule(x, y, radius, color, delta_x, delta_y))
    
    def update_balls(self):
        # Обновляем позиции всех шариков
        for molecule in self.molecules:
            molecule.move(self.width(), self.height())
        
        # Перерисовываем виджет
        self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Рисуем все шарики
        for molecule in self.molecules:
            molecule.draw(painter)