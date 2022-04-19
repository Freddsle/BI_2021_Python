import threading
import time


threads = [threading.Thread(target=time.sleep, args=(10,)) for _ in range(10)]
for thread in threads:
    thread.start()
print("Main thread!")
