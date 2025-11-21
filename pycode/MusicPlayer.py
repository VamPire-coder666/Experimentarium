from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl


class MusicPlayer(QMediaPlayer):
    """Класс для воспроизведения музыки
    """
    
    def __init__(self, mode='main', parent=None):
        super().__init__(parent)
        self.audio = QAudioOutput()
        self.setAudioOutput(self.audio)
        if mode == 'main':
            self.setSource(QUrl.fromLocalFile('resources/MAIN_Hidden_Orchestra_-_Attic.mp3'))