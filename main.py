#!/usr/bin/env python3
# encoding: utf-8

"""
Основной скрипт программы.
Запускает конфигуратор окна, подключает слоты и отображает окно.
"""

# Импортируем модули
try:
    from sys import argv, exit
    from threading import Thread
    from queue import Queue
#    from PyQt5.QtCore import QTimer
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
    from cv2 import VideoCapture, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT
    # Импортируем класс со слотами
    from ui.mainwindow_slots import Slots_MainWindow
except ImportError:
    print("Please install the required packages.")
    exit()

global q
q = Queue()

# Граббер камеры
def grab(cam, queue, width, height):
    global running
    capture = VideoCapture(cam)
    capture.set(CAP_PROP_FRAME_WIDTH, width)
    capture.set(CAP_PROP_FRAME_HEIGHT, height)

    while(running):
        frame = {}
        capture.grab()
        retval, img = capture.retrieve(0)
        frame["img"] = img
        queue.put(frame)

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
        self.Timer.timeout.connect(self.update_frame(q))
        return None

if __name__ == '__main__':

    capture_thread = Thread(target=grab, args=(0, q, 640, 360))

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

