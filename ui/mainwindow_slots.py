#!/usr/bin/env python
# encoding: utf-8

"""
Пользовательские слоты для виджетов.
"""

# Импортируем модули
try:
    from sys import exit
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
        print("Exec")
        self.Label.setPixmap(QPixmap.fromImage("../image.jpg"))
        return None
