from multiprocessing import Process, Queue
import os
import random

def affichagep(pidf,):
    print("hello World!")
    print("Mon PID est "+str(os.getpid())+" et celui de mon fils est "+str(pidf))
    #os.getpid affiche le pid du fils
    #os.getppid affiche le pid du père
def affichage():
    print("hello World!")
    print("Mon PID est "+str(os.getpid())+" et celui de mon père est "+str(os.getppid()))


if __name__ == "__main__":
    p1 = Process(target=affichage)
    
    p1.start()
    status=os.wait()
    pidfils = (status[0])
    val = status[1]

affichagep(pidfils)