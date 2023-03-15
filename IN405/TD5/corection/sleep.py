#!/usr/bin/python3

import multiprocessing as mp
import os
import random

def alea():
    value = random.randrange(1, 50)
    print("J'ai choisi %d !" % (value))
    exit(value)

if __name__ == '__main__':
    p = mp.Process(target=alea)
    p.start()
    p.join()
    print("Il a choisi %d !" % (p.exitcode))
