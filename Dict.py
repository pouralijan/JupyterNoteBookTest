#!/usr/bin/env python3
# coding: utf-8

# In[15]:


import threading
import pyperclip
import time

def print_to_stdout(clipboard_content):
    print (str(clipboard_content))

class ClipboardWatcher(threading.Thread):
    def __init__(self, callback):
        super(ClipboardWatcher, self).__init__()
        self._callback = callback
        self._stopping = False

    def run(self):       
        recent_value = pyperclip.paste()
        while not self._stopping:
            tmp_value = pyperclip.paste()
            if tmp_value != recent_value:
                recent_value = tmp_value
                self._callback(recent_value)
    def stop(self):
        self._stopping = True

watcher = ClipboardWatcher(print_to_stdout)
watcher.start()

