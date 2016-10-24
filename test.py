#!/usr/bin/env python
# encoding: utf-8

import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Queue import *
import cv2


def GrabCam(cam, queue, width, height):
    # Источник
    capture = cv2.VideoCapture(cam)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    # Проверка подключения к камере
    if not capture.isOpened():
        print("could not open cam:", cam)
        return

    while (running):
        frame = {}
        capture.grab()
        retval, img = capture.retrieve(0)
        frame["img"] = img

        if queue.qsize() < 10:
            queue.put(frame)
        else:
            print(queue.qsize())


class ImageViewer(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.filename = "./flughahn.jpg"
        self.setup_ui()

    def setup_ui(self):
        img = cv2.imread(self.filename)
        self.image_label = QLabel()
        if img is None:
            self.image_label.setText("Cannot load the input image.")
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_ = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
            self.image_label.setPixmap(QPixmap.fromImage(img_))
        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.close)
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.main_layout.addWidget(self.quit_button)
        self.setLayout(self.main_layout)
        self.setWindowTitle("OpenCV - Qt Integration")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()

    q = Queue()
    capture_thread = threading.Thread(target=GrabCam, args=(0, q, 960, 540))

    app.exec_()