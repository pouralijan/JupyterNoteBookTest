#!/usr/bin/env python3
import threading
import time
import logging


def daemon():
    logging.debug('Starting')
    time.sleep(4)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiiiiiiiiiiiiiiiiiiiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
d.join(.2)
print('d.isAlive()', d.isAlive())
t.join()
