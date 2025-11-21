from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, \
    QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPainter, QPixmap
from .db_functions import *
from .HelpWindow import HelpWindow
import io
from sheets_py.experiment_window_sheet import experiment_window_sheet


class ErrorDialog(QDialog):
    """ Диалог для вывода ошибки """
    
    def __init__(self, text, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Ошибка")
        self.setWindowIcon(QIcon("resources/vampire_bat.png"))
        self.setStyleSheet("background-color: #2a3943")

        QBtn = (
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel(text)
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)



class ExperimentWindow(QWidget):
    """ Базовый класс эксперимента """
    
    def __init__(self, main_window, template):
        super().__init__()
        self.main_window = main_window
        self.setWindowIcon(QIcon("resources/vampire_bat.png"))
        uic.loadUi(io.StringIO(template), self)
    
    def initUI(self):
        self.setStyleSheet(experiment_window_sheet)
        self.save_pushButton.clicked.connect(self.save)
        self.expname_lineEdit.textChanged.connect(self.rename)
        self.escape_pushButton.clicked.connect(self.return_to_main)
        self.delete_btn.clicked.connect(self.delete)
        self.help_btn.clicked.connect(self.help)
        self.pixmap = QPixmap("resources/background.png")
        self.figures = 0
    
    def help(self):
        """ Вывод окна для помощи """
        
        self.hide()
        self.sec_window = HelpWindow(self)
        self.sec_window.show()
    
    def delete(self):
        """ Удаление эксперимента """
        
        delete_experiment(self)
        self.main_window.show()
        self.close()
    
    def set_params(self, name, login):
        pass
    
    def save(self):
        """ Сохранение эксперимента """
        
        yn, message = save_experiment(self)
        self.status.setText(message)
        if not yn:
            self.status.setStyleSheet('background: rgb(150, 0, 0)')
        else:
            self.status.setStyleSheet('')
        self.status.show()
    
    def rename(self):
        """ Переименование эксперимента """
        
        self.setWindowTitle(self.expname_lineEdit.text())
    
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
    
    def return_to_main(self):
        """ Возврат к главному окну """
        
        self.main_window.update()
        self.main_window.show()
        self.close()