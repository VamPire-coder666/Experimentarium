from pycode.ExperimentClasses import ExperimentWindow, ErrorDialog
from .BallisticShow import BallisticShow
from .MainBallisticShow import MainBallisticShow
from .environments import ENV
from PyQt6.QtWidgets import QWidget, QInputDialog, QColorDialog
from pycode.db_functions import save_ballistic_exp, get_experiment
from .BallisticFigure import BallisticFigure
from templates_py.ballistic_exp_window import ballistic_exp_window
from .ChangeThemeWindow import ChangeThemeWindow


class BallisticExpWindow(ExperimentWindow):
    """ Класс эксперимента по баллистике

    Args:
        main_window (MyMainWindow): главное окно приложения
    """
    
    def __init__(self, main_window):
        super().__init__(main_window, ballistic_exp_window)
        self.initUI()
    
    def initUI(self):
        """ Вспомогательная функция авторизации """
        
        super().initUI()
        self.sec_window = QWidget()
        self.flag = False
        self.type = 'ballistic'
        self.show_type = 'one'
        self.start_btn.clicked.connect(self.start)
        self.env_comboBox.addItems(ENV.keys())
        self.g = 9.807

        self.status.setStyleSheet('')
        
        self.add_figure_btn.clicked.connect(self.add_figure)
        self.open_exp_btn.clicked.connect(self.main_window.open_experiment)
        self.change_view_btn.clicked.connect(self.change_result_theme)
        
        self.env_comboBox.currentTextChanged.connect(self.edit_g)
        
        self.mass_spinBox.valueChanged.connect(self.update_figures)
        self.speed_spinBox.valueChanged.connect(self.update_figures)
        self.corner_spinBox.valueChanged.connect(self.update_figures)
        self.open_exp_btn.clicked.connect(self.main_window.open_experiment)
        
        # Показываем скрытые виджеты
        self.figure_label.hide()
        self.mass_label.hide()
        self.mass_spinBox.hide()
        self.speed_label.hide()
        self.speed_spinBox.hide()
        self.corner_label.hide()
        self.corner_spinBox.hide()
        self.color_lineEdit.hide()
        self.color_label.hide()

    def change_result_theme(self):
        self.sec_window = ChangeThemeWindow(self)
        self.sec_window.show()
    
    def edit_g(self):
        # Изменение среды полёта
        self.g = ENV[self.env_comboBox.currentText()]
    
    def close(self):
        # Перед закрытием закрываем вспомогательные окна
        self.sec_window.close()
        super().close()
    
    def save(self):
        """ Сохранение """
        yn, message = save_ballistic_exp(self)
        self.status.setText(message)
        if not yn:
            self.status.setStyleSheet('background: rgb(150, 0, 0)')
        else:
            self.status.setStyleSheet('')
        self.status.show()
    
    def update_figures(self):
        """Обновление тел"""
        mass, speed, corner = self.mass_spinBox.value(), self.speed_spinBox.value(), self.corner_spinBox.value()
        color = self.figures_textbrowser.toPlainText().split(', ')[-1]
        template = f"""<p>{self.figures}, {mass}кг, {speed}м/с, {corner}°, {color}</p>"""
        self.figures_textbrowser.setHtml(template)
    
    def start(self):
        """ Запуск эксперимента """
        
        if not self.figures_textbrowser.toPlainText():
            self.status.setStyleSheet("background: rgb(150, 0, 0)")
            self.status.setText('В эксперименте должны быть тела')
            return

        self.sec_window.close()
        self.g = ENV[self.env_comboBox.currentText()]
        self.figure = BallisticFigure(
            self.mass_spinBox.value(), self.speed_spinBox.value(),
            self.corner_spinBox.value(), self.color_lineEdit.text()
            )
        if self.show_type == 'one':
            self.sec_window = MainBallisticShow(self.figure, self.g, self)
        else:
            self.sec_window = BallisticShow(self.figure, self.g, self)
        self.sec_window.show()
    
    def add_figure(self):
        """Добавдение тел"""
        if self.figures_textbrowser.toPlainText():
            dlg = ErrorDialog("В данном эксперименте можно создать только одно тело.\nХотите изменить его?", self)
            if dlg.exec():
                pass
            else:
                return
        mass, ok_pressed = QInputDialog.getInt(
            self, "Введите параметры тела", "Какова масса тела?, кг",
            0, 0, 1000000000, 1
        )
        if not ok_pressed:
            return
        self.mass_label.show()
        self.mass_spinBox.show()
        self.mass_spinBox.setValue(mass)
        
        speed, ok_pressed = QInputDialog.getInt(
            self, "Введите параметры тела", "Каков модуль скорости тела?, м/с",
            0, 0, 300000000, 1
        )
        if not ok_pressed:
            return
        self.speed_label.show()
        self.speed_spinBox.show()
        self.speed_spinBox.setValue(speed)
        
        corner, ok_pressed = QInputDialog.getInt(
            self, "Введите параметры тела", "Каков угол между вектором скорости и осью OX?, градусы",
            0, 0, 360, 1
        )
        if not ok_pressed:
            return
        self.corner_label.show()
        self.corner_spinBox.show()
        self.corner_spinBox.setValue(corner)
        
        color = QColorDialog.getColor()
        if color.isValid():
            color = color.name()
            self.color = (int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16))
        else:
            return
        self.color_label.show()
        self.color_lineEdit.show()
        self.color_lineEdit.setText(color)
        
        self.figures += 1
        template = f"""<p>{self.figures}, {mass}кг, {speed}м/с, {corner}°, {color}</p>"""
        self.figures_textbrowser.setHtml(template)
        self.figure = BallisticFigure(mass, speed, corner, color)
    
    def set_params(self, name, login):
        """ Установка параметров для эксперимента
        (загрузка эксперимента)

        Args:
            name (str): имя пользователя
            login (str): логин пользователя
        """
        
        super().set_params(name, login)
        
        params = get_experiment(name, login)
        
        self.expname_lineEdit.setText(params[2])
        self.env_comboBox.setCurrentText(params[4])
        self.figures_textbrowser.setHtml(params[5])
        if params[-1] != 'None':
            self.comments_textEdit.setPlainText(params[-1])
        
        num, mass, speed, corner, color = self.figures_textbrowser.toPlainText().split(', ')
        mass = int(mass[:-2])
        speed = int(speed[:-3])
        corner = int(corner[:-1])
        self.g = ENV[self.env_comboBox.currentText()]
        data = self.figures_textbrowser.toPlainText().split(', ')
        
        self.color_label.show()
        self.color_lineEdit.show()
        self.color_lineEdit.setText(data[4])
        
        self.corner_label.show()
        self.corner_spinBox.show()
        self.corner_spinBox.setValue(int(data[3][:-1]))
        
        self.speed_label.show()
        self.speed_spinBox.show()
        self.speed_spinBox.setValue(int(data[2][:-3]))
        
        self.mass_label.show()
        self.mass_spinBox.show()
        self.mass_spinBox.setValue(int(data[1][:-2]))
        
        self.figure = BallisticFigure(mass, speed, corner, color)