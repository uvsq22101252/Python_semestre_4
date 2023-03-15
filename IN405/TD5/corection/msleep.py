#!/usr/bin/python3

import multiprocessing as mp
from multiprocessing import connection
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

while len(pool):
    mappool = {p.sentinel: p for p in pool}
    done = connection.wait(mappool.keys())
    for elt in done:
        mappool[elt].join()
        print("[prnt] process %d done" % (mappool[elt].pid))
        pool.remove(mappool[elt])
