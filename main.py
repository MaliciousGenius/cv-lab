#!/usr/bin/env python3
# encoding: utf-8

"""
Основной скрипт программы.
Запускает конфигуратор окна, подключает слоты и отображает окно.
"""

# Импортируем модули
try:
    from sys import argv, exit
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
    from multiprocessing import Queue
    # Импортируем класс со слотами
    from ui.mainwindow_slots import Slots_MainWindow
    from vision import producer
except ImportError:
    print("Please install the required packages.")
    exit()

# Создаём класс основного окна, наследуясь от класса со слотами.
class MainWindow(Slots_MainWindow):

    # При инициализации класса нам необходимо выпонить некоторые операции
    def __init__(self, window):
        # Сконфигурировать интерфейс методом из базового класса Ui_MainWindow
        self.setupUi(window)
        # Подключить созданные нами слоты к виджетам
        self.connect_slots()

    # Подключаем слоты к виджетам
    def connect_slots(self):
        self.Show.clicked.connect(self.show)
        return None

if __name__ == '__main__':

    q = Queue()

    # Создаём экземпляр приложения
    app = QApplication(argv)

    # Создаём базовое окно, в котором будет отображаться наш UI
    window = QMainWindow()

    # Создаём экземпляр нашего UI
    ui = MainWindow(window)

    # Отображаем окно
    window.show()

    # Обрабатываем нажатие на кнопку окна "Закрыть"
    exit(app.exec_())

