#!/usr/bin/python3

import multiprocessing as mp
import os
import random
import time

def go_sleep():
    value = random.randrange(1, 10)
    time.sleep(value)
    print("[%d] awoken after %ds" % (mp.current_process().pid, value))

pool = [mp.Process(target=go_sleep) for _ in range(10)]

for elt in pool:
    elt.start()

for _ in range(10):
    pid, _ = os.wait()
    print("[prnt] process %d done" % (pid))

for elt in pool:
    elt.join()