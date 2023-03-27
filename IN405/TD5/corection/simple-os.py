#!/usr/bin/python3

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
    print('[%d] J\'ai choisi %d !' % (os.getpid(), value))
    exit(value)

if __name__ == '__main__':
    if os.fork() == 0:
        alea()
    else:
        pid, val = os.wait()
        # val est un status d'erreur écrit sur 16 bits, le code de retour est
        # contenu dans les 8 bits de poids forts, donc décalage à droite
        print('[%d] {%d} a choisi %d !' % (os.getpid(), pid, val >> 8))
