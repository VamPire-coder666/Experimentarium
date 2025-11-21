from PyQt6 import QtCore, QtWidgets
import sys
import os
from PyQt6.QtWidgets import QApplication
from pycode.MyMainWindow import MyMainWindow

'''
На экранах с высоким разрешением некоторые интерфейсы,
разработанные для стандартного разрешения, могут выглядеть не корректно или мелко.
Один из способов решения проблемы(два условия ниже).
'''
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


# Для того чтобы видеть ошибки
def except_hook(cls, exception, traceback):
    """Функция для обработки ошибок PyQT"""
    sys.__excepthook__(cls, exception, traceback)


def main():
    try:
        os.system('clear')
        # Создадим класс приложения PyQT
        app = QApplication(sys.argv)
        # Объект класса MyMainWindow - главное окно
        ex = MyMainWindow()
        sys.excepthook = except_hook
        # Будем ждать, пока пользователь не завершил исполнение QApplication,
        # а потом завершим и нашу программу
        print('Window opened...')
        sys.exit(app.exec())
    except SystemExit:
        # После закртыия пишем, что завершили работу
        print('Window was closed')


if __name__ == '__main__':
    main()