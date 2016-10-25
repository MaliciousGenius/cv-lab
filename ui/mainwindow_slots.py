#!/usr/bin/env python3
# encoding: utf-8

"""
Пользовательские слоты для виджетов.
"""

# Импортируем модули
try:
    from sys import exit
    from time import sleep
#    from cv2 import imread, cvtColor, COLOR_BGR2RGB
    from PyQt5.QtGui import QPixmap, QImage
    from PyQt5.QtWidgets import QLabel
    # Импортируем класс интерфейса из созданного конвертером модуля
    from ui.mainwindow import Ui_MainWindow
except ImportError:
    print("Please install the required packages.")
    exit()

# Создаём собственный класс, наследуясь от автоматически сгенерированного
class Slots_MainWindow(Ui_MainWindow):

    # Определяем пользовательский слот
    def show(self):
        self.Label.setPixmap(QPixmap("./ui/image.jpg"))
        return None


    def update_frame(self, q):
        sleep(5)
        if not q.empty():
            frame = q.get()
            img = frame["img"]
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            height, width, bpc = img.shape
            bpl = bpc * width
            image = QImage(img.data, width, height, bpl, QImage.Format_RGB888)
            self.Label.setPixmap(QPixmap(image))
            return None

