from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QPainter, QIcon
from PyQt6.QtCore import Qt
import io
from templates_py.help_window import help_window
from sheets_py.help_window_sheet import help_window_sheet
from resources.help_html_text import HTML


class HelpWindow(QWidget):
    """ Окно для вывода краткой инструкции(помощь) """
    
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        uic.loadUi(io.StringIO(help_window), self)
        self.setWindowIcon(QIcon("resources/vampire_bat.png"))
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet(help_window_sheet)
        self.textBrowser.setHtml(HTML)
        self.textBrowser.setOpenExternalLinks(True)
        self.pixmap = QPixmap('resources/help_photo.jpg')
        self.return_btn.clicked.connect(self.return_to_main)
    
    def return_to_main(self):
        """ Возврат к главному окну """
        
        self.main_window.show()
        self.close()
    
    def paintEvent(self, event):
        """ Функция для отрисовки изображения
        Args:
            event (_type_): Событие
        """
        painter = QPainter(self)
        # Масштабируем изображение под размер виджета
        scaled_pixmap = self.pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        painter.drawPixmap(0, 0, scaled_pixmap)