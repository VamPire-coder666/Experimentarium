from PyQt6.QtWidgets import QWidget, QLineEdit
from PyQt6 import uic
import io
from PyQt6.QtGui import QIcon, QPainter, QPixmap
from PyQt6.QtCore import Qt
from .db_functions import *
from .myhash import user_to_db, fhash
from .HelpWindow import HelpWindow
from .check_password import check_password
from templates_py.authorization import authorization
from templates_py.registration import registration
from sheets_py.authorization_window_sheet import authorization_window_sheet


class AuthorizationWindow(QWidget):
    '''Класс для авторизации при запуске главного окна'''
    
    def __init__(self, parent):
        super().__init__()
        self.main_window = parent
        self.setWindowIcon(QIcon("resources/vampire_bat.png"))
        uic.loadUi(io.StringIO(authorization), self)
        self.initUI()
    
    def initUI(self):
        """ Вспомогательная функция для инициализации """
        
        self.setStyleSheet(authorization_window_sheet)
        self.help_btn.clicked.connect(self.help)
        self.password_lineEdit.returnPressed.connect(self.sign_in)
        self.close_btn.clicked.connect(self.close)
        self.sign_in_btn.clicked.connect(self.sign_in)
        self.sign_up_btn.clicked.connect(self.sign_up)
        self.checkBoxShowPassword.stateChanged.connect(
            self.toggle_password_visibility)
        self.pixmap = QPixmap("resources/background.png")
    
    def help(self):
        """ Function open's a HelpWindow """
        
        self.sec_window = HelpWindow(self)
        self.hide()
        self.sec_window.show()
    
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
    
    def sign_in(self):
        login, password, error =  self.is_logged()
        if login and password:
            self.main_window.show()
            self.main_window.login = self.login_lineEdit.text()
            self.close()
        else:
            error = f'<html><head/><body><p><span style=" font-size:24pt;">{error}</span></p></body></html>'
            self.label.setText(error)
            if not login:
                self.login_lineEdit.setStyleSheet('background: rgb(150, 0, 0)')
            else:
                self.login_lineEdit.setStyleSheet('')
            if not password:
                self.password_lineEdit.setStyleSheet('background: rgb(150, 0, 0)')
            else:
                self.password_lineEdit.setStyleSheet('')
    
    def sign_up(self):
        self.main_window.sec_window = SignUpWindow(self.main_window)
        self.main_window.sec_window.show()
        self.close()
    
    def is_logged(self):
        login = self.login_lineEdit.text()
        password = self.password_lineEdit.text()
        if not login and not password:
            return False, False, 'Все поля должны быть заполнены!'
        elif not login:
            return False, True, 'Все поля должны быть заполнены!'
        elif not password:
            return True, False, 'Все поля должны быть заполнены!'
        else:
            if login in get_logins():
                if get_logins_passwords()[login] == fhash(password):
                    return True, True, None
                else:
                    return True, False, 'Неправильный пароль'
            return False, True, 'Нет такого логина'
    
    def toggle_password_visibility(self, state):
        """ Переключает видимость пароля """
        if state == Qt.CheckState.Checked.value:
            self.password_lineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)


class SignUpWindow(QWidget):
    '''Класс для регистрации'''
    
    def __init__(self, parent):
        super().__init__()
        self.setWindowIcon(QIcon("resources/vampire_bat.png"))
        self.main_window = parent
        uic.loadUi(io.StringIO(registration), self)
        self.initUI()
    
    def initUI(self):
        # Такой же стиль, как и для авторизации
        self.setStyleSheet(authorization_window_sheet)
        self.help_btn.clicked.connect(self.help)
        self.password_lineEdit.returnPressed.connect(self.sign_up)
        self.checkBoxShowPassword.stateChanged.connect(
            self.toggle_password_visibility)
        self.return_btn.clicked.connect(self.return_to_au)
        self.sign_up_btn.clicked.connect(self.sign_up)
        self.pixmap = QPixmap("resources/background.png")
    
    def help(self):
        """ Function open's a HelpWindow """
        
        self.sec_window = HelpWindow(self)
        self.hide()
        self.sec_window.show()
        
            
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
    
    def sign_up(self):
        tr_fl, error, *password_error = self.log_in()
        if tr_fl:
            self.main_window.show()
            self.main_window.login = self.login_lineEdit.text()
            self.close()
        else:
            if error == 'Все поля должны быть заполнены!':
                if not self.name_lineEdit.text():
                    self.name_lineEdit.setStyleSheet('background: rgb(150, 0, 0)')
                else:
                    self.name_lineEdit.setStyleSheet('')
                if not self.surname_lineEdit.text():
                    self.surname_lineEdit.setStyleSheet('background: rgb(150, 0, 0)')
                else:
                    self.surname_lineEdit.setStyleSheet('')
                if not self.login_lineEdit.text():
                    self.login_lineEdit.setStyleSheet('background: rgb(150, 0, 0)')
                else:
                    self.login_lineEdit.setStyleSheet('')
                if not self.password_lineEdit.text():
                    self.password_lineEdit.setStyleSheet('background: rgb(150, 0, 0)')
                else:
                    self.password_lineEdit.setStyleSheet('')
            elif error == 'Такой логин уже есть':
                self.login_lineEdit.setStyleSheet('background: rgb(150, 0, 0)')
            elif password_error:
                error = password_error[0]
                self.password_lineEdit.setStyleSheet('background: rgb(150, 0, 0)')
            error = f'<html><head/><body><p><span style=" font-size:24pt;">{error}</span></p></body></html>'
            self.label_1.setText(error)
    
    def log_in(self):
        name = str(self.name_lineEdit.text())
        surname = str(self.surname_lineEdit.text())
        login = str(self.login_lineEdit.text())
        password = str(self.password_lineEdit.text())
        if not all(map(lambda x: x, (name, surname, login, password))):
            return False, 'Все поля должны быть заполнены!'
        if login in get_logins():
            return False, 'Такой логин уже есть'
        ok, error = check_password(password)
        if not ok:
            return False, None, error
        user_to_db(login, password, name, surname)
        self.name, self.surname = name, surname
        return True, None
    
    def return_to_au(self):
        self.main_window.sec_window = AuthorizationWindow(self.main_window)
        self.main_window.sec_window.show()
        self.close()
    
    def toggle_password_visibility(self, state):
        """ Переключает видимость пароля """
        if state == Qt.CheckState.Checked.value:
            self.password_lineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)