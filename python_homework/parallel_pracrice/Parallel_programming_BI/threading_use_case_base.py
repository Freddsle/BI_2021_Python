import time

import keyboard


number = 0
while True:
    print(number)
    time.sleep(1)
    number = keyboard.read_key()
