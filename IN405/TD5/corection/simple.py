#!/usr/bin/python3

import multiprocessing as mp
import os
import random

def hello():
    print('Hello World!')

def father(pid):
    print('Mon PID est %d et celui de mon fils est %d !' % (os.getpid(), pid))

def child():
    print('Mon PID est %d et celui de mon pere est %d !' % (os.getpid(),
                                                            os.getppid()))

def alea():
    value = random.randrange(1, 50)
    print('Jai choisi %d !' % (value))
    exit(value)

if __name__ == '__main__':
    p = mp.Process(target=alea)
    p.start()
    p.join()
    print('Il a choisi %d !' % (p.exitcode))
