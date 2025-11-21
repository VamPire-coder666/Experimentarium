from PyQt6.QtWidgets import QMainWindow, QInputDialog
from .AuWindowClasses import *
from .Ballistic.BallisticMain import BallisticExpWindow
from .HelpWindow import HelpWindow
from .Music_Window import Music_Window
from .MusicPlayer import MusicPlayer
from templates_py.main_window import main_window
from sheets_py.main_window_sheet import main_window_sheet


class MyMainWindow(QMainWindow):
    """
    Главное окно приложения
    """
    
    def __init__(self):
        super().__init__()
        uic.loadUi(io.StringIO(main_window), self)
        self.setWindowIcon(QIcon("resources/vampire_bat.png"))
        # При инициализации запускается окно авторизации - главное окно скрыто до авторизвции
        self.sec_window = AuthorizationWindow(self)
        self.sec_window.show()
        self.initUI()
    
    def initUI(self):
        """ Вспомагательная функция авторизации """
        
        self.setStyleSheet(main_window_sheet)
        
        self.statusbar = self.statusBar()
        
        self.player = MusicPlayer('main', self)
        self.player.setLoops(-2)
        self.player.audio.setVolume(0.5)
        self.player.play()
        
        self.music_btn.clicked.connect(self.change_music)
        self.help_btn.clicked.connect(self.help)
        self.my_experiments_btn.clicked.connect(self.open_experiment)
        self.new_experiment_btn.clicked.connect(self.new_experiment)
        self.close_btn.clicked.connect(self.close)
        self.escape_btn.clicked.connect(self.return_to_au)

        self.new_exp_action.triggered.connect(self.new_experiment)
        self.new_exp_action.setShortcut('Ctrl+N')
        self.my_exp_action.triggered.connect(self.open_experiment)
        self.my_exp_action.setShortcut('Ctrl+O')
        self.escape_action.triggered.connect(self.return_to_au)
        self.escape_action.setShortcut('Ctrl+Z')
        self.close_action.triggered.connect(self.close)
        self.close_action.setShortcut('Ctrl+Q')

        self.pixmap = QPixmap("resources/background.png")
    
    def close(self):
        """Закрытие окна
        """
        
        # Перед закрытием закрываем другие окна
        self.sec_window.close()
        super().close()
    
    def change_music(self):
        """Открытие окна для изменения музыки
        """
        
        self.sec_window = Music_Window(self)
        self.sec_window.show()
    
    def open_experiment(self):
        """
        Открытие экспериментов
        """
        
        # Читаем эксперименты пользователя
        exps = get_experiments(self.login)
        # Если у пользователья нет експериментов - завершаем работу и выводим ошибку в statusbar
        if not exps:
            self.statusbar.setStyleSheet('background: rgb(150, 0, 0)')
            self.statusbar.showMessage('У вас нет экспериментов!')
            return
        else:
            self.statusbar.setStyleSheet('')
        # Спрашиваем нужный эксперимент
        name, ok_pressed = QInputDialog.getItem(
            self, "Выберите Эксперимент", "Какой эксперимент надо загрузить?",
            tuple(exps), editable=False
            )
        # Если пользователь выбрал - открываем эксперимент
        if ok_pressed:
            exp = list(filter(lambda x: x == name, exps))[0]
            if exp:
                self.load_experiment(exp)
                self.statusbar.setStyleSheet('')
            else:
                # Пишем, если что-то не так
                self.statusbar.setStyleSheet('background: rgb(150, 0, 0)')
                self.statusbar.showMessage('Что-то пошло не так!')
    
    def load_experiment(self, name):
        """
        Функция для загрузки выбранного эксперимента
        
        Args:
            params(list): список-описание экспериментов - [login, name, env, figures, comments]
        """
        
        self.sec_window = BallisticExpWindow(self)
        self.sec_window.set_params(name, self.login) # Загружаем параметры эксперимента
        self.sec_window.show()
        self.hide()
    
    def help(self):
        """Функция для открытия окна помощи
        """
        
        self.hide()
        self.sec_window = HelpWindow(self)
        self.sec_window.show()
    
    def new_experiment(self):
        """
        Создание нового эксперимента
        """
        self.hide()
        self.sec_window = BallisticExpWindow(self)
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
        
        self.statusbar.setStyleSheet('')
        self.statusbar.clearMessage()
    
    def return_to_au(self):
        """
        Выход из аккаунта
        """
        self.sec_window = AuthorizationWindow(self)
        self.sec_window.show()
        self.hide()