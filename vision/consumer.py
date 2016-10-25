#!/usr/bin/env python3
# encoding: utf-8

"""
"""

# Импортируем модули
try:
    from sys import exit
    from time import sleep
    from multiprocessing import Process
    from cv2 import imshow, waitKey
    from queue import Queue
except ImportError:
    print("Please install the required packages.")
    exit()

def ConsumerWorker(queue):
    while True:
        if not queue.empty():
            # Захват кадра
            frame = queue.get()

            # Показ кадра
            imshow('frame', frame)
        else:
            print("Очередь пуста")
            sleep(10)

if __name__ == '__main__':
    q = Queue()

    consumer = Process(target=ConsumerThread, args=(q,))
    consumer.start()
    consumer.join()