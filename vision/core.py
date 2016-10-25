#!/usr/bin/env python3
# encoding: utf-8

"""
"""

# Импортируем модули
try:
    from sys import exit
    from multiprocessing import Queue
    from queue import Queue
except ImportError:
    print("Please install the required packages.")
    exit()

if __name__ == '__main__':
    q = Queue()

    producer = Process(target=ProducerWorker, args=(q,))
    producer.start()

    consumer = Process(target=ConsumerWorker, args=(q,))
    consumer.start()