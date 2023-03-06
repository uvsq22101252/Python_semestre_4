from multiprocessing import Process
import os
def print_hello():
    print("hello World!")

def print_PID(p1,p2):

    print("Mon PID est "+str(os.getpid(p1))+" et celui de mon pere/fils est "+str(os.getppid(p2))


if __name__ == "__main__":
    p1 = Process(target=print_hello, args=)
    p2 = Process(target=print_hello)
    #start process
    p1.start()
    p2.start()
    #wait until process is finished
    p1.join()
    p2.join()

