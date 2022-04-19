from threading import Thread
import time

import keyboard


class KeyboardListener(Thread):
    def __init__(self, active_number):
        super().__init__()
        self.active_number = active_number

    def run(self):
        while True:
            self.active_number = keyboard.read_key()


number = "0"
listener = KeyboardListener(number)
listener.start()
while True:
    print(number)
    time.sleep(1)
    number = listener.active_number
