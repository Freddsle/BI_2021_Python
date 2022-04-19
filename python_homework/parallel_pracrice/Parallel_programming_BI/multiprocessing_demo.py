import random
import multiprocessing


def do_work():
    for _ in range(100000000):
        random.randint(1, 40) ** random.randint(1, 20)


procs = [multiprocessing.Process(target=do_work) for i in range(3)]
for proc in procs:
    proc.start()

do_work()