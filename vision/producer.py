#!/usr/bin/env python3
# encoding: utf-8

"""
"""

# Импортируем модули
try:
    from sys import exit
    from time import sleep
    from multiprocessing import Process, Queue
    from cv2 import VideoCapture
#    from queue import Queue
except ImportError:
    print("Please install the required packages.")
    exit()

def ProducerWorker(queue):
    # Источник
    capture = VideoCapture(0)

    # Проверка подключения к камере
    if not capture.isOpened():
        print("Неудалось подключиться к камере")
        return

    while True:
        # Захват фрейма
        _, frame = capture.read()

        # Запись в фрейма в очередь
        queue.put(frame)


if __name__ == '__main__':
    q = Queue()

    producer = Process(target=ProducerWorker, args=(q,))
    producer.start()
    producer.join()