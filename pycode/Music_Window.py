from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap, QImage, QIcon
from PyQt6 import uic
from PyQt6.QtCore import QUrl
import io
from templates_py.music_window import music_window


class Music_Window(QWidget):
    """ Окно для изменения музыки """
    
    def __init__(self, parent):
        super().__init__()
        self.main_window = parent
        uic.loadUi(io.StringIO(music_window), self)
        self.setWindowIcon(QIcon("resources/vampire_bat.png"))

        self.volume_Slider.valueChanged.connect(self.change_volume)
        self.volume_Slider.setValue(50)
        self.stopmusic_checkBox.stateChanged.connect(self.mute)

        self.pixmap1.setPixmap(QPixmap.fromImage(QImage('resources/attic_pixmap.jpg').scaled(60, 50)))
        self.pixmap2.setPixmap(QPixmap.fromImage(QImage('resources/aria_math_pixmap.jpg').scaled(60, 50)))
        self.pixmap3.setPixmap(QPixmap.fromImage(QImage('resources/Star_Wars_Logo.jpg').scaled(60, 50)))
        self.pixmap4.setPixmap(QPixmap.fromImage(QImage('resources/dark_fantasy_pixmap.jpg').scaled(60, 50)))
        self.pixmap5.setPixmap(QPixmap.fromImage(QImage('resources/machinarium.jpg').scaled(60, 50)))

        self.attic_btn.clicked.connect(self.change_music_attic)
        self.aria_math_btn.clicked.connect(self.change_music_aria)
        self.clones_btn.clicked.connect(self.change_music_clones)
        self.machinarium_btn.clicked.connect(self.change_music_machinarium)
        self.darkfantasy_btn.clicked.connect(self.change_music_dark_fantasy)

        self.return_btn.clicked.connect(self.close)
    
    def change_music_machinarium(self):
        """ Функция для изменения музыки на Machinarium """
        
        self.main_window.player.setSource(QUrl.fromLocalFile('resources/Machinarium_-_One.mp3'))
        self.main_window.player.play()
    
    def change_music_dark_fantasy(self):
        """ Функция для изменения музыки на dark fantasy """
        
        self.main_window.player.setSource(QUrl.fromLocalFile('resources/voidseer._-_dark_fantasy.mp3'))
        self.main_window.player.play()
    
    def change_music_clones(self):
        """ Функция для изменения музыки на March of Clones """
        
        self.main_window.player.setSource(QUrl.fromLocalFile('resources/Star_Wars-Clones.mp3'))
        self.main_window.player.play()
    
    def change_music_aria(self):
        """ Функция для изменения музыки на Aria Math """
        
        self.main_window.player.setSource(QUrl.fromLocalFile('resources/FRXN_-_Aria_math_phonk.mp3'))
        self.main_window.player.play()
    
    def change_music_attic(self):
        """ Функция для изменения музыки на Attic """
        
        self.main_window.player.setSource(QUrl.fromLocalFile('resources/MAIN_Hidden_Orchestra_-_Attic.mp3'))
        self.main_window.player.play()
    
    def change_volume(self):
        """ Изменение звука """
        
        self.main_window.player.audio.setVolume(self.volume_Slider.value() / 100)
    
    def mute(self):
        """ Выключение звука """
        
        if self.stopmusic_checkBox.isChecked():
            self.main_window.player.audio.setVolume(0.00)
        else:
            self.main_window.player.audio.setVolume(self.volume_Slider.value() / 100)