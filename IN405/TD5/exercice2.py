from multiprocessing import Process
import os
import random

def print_hello():
    print("hello World!")
    print_PID()
    random_value()

def print_PID():

    print("Mon PID est "+str(os.getpid())+" et celui de mon père est "+str(os.getppid()))
    #os.getpid affiche le pid du fils
    #os.getppid affiche le pid du père
def random_value():
    if os.getpid()!= 0:
        value = random.randint(0,100)
        print(value)


    
print_hello()

if __name__ == "__main__":
    p1 = Process(target=print_hello)
    #start process
    p1.start()
    #wait until process is finished
    p1.join()

