import threading
import argparse
from random import randint


def initialisation_message(indice,mail,lock,condition):
    val = randint(0,100)
    print("j'ai séléctionné: %d"%(val))
    mail[indice] = val
    lock[indice].acquire()
    condition[indice].notify()
    lock[indice].release()

def transfer_message(indice,mail,lock,condition):
    with lock[indice-1]:
        condition[indice-1].wait()
    mail[indice] = mail[indice-1]
    with lock[indice]:
        condition[indice].notify()
def fin_message(indice,mail,lock,condition):
    lock[indice-1].acquire()
    condition[indice-1].wait()
    lock[indice-1].release()
    print("j'ai reçu: %d" %(mail[indice-1]))

if __name__ == "__main__":
    argP = argparse.ArgumentParser()
    argP.add_argument("nbr_thread",type=int)
    args = argP.parse_args()

    lock = [threading.Lock() for i in range(args.nbr_thread+1)]
    condition = [threading.Condition(lock[i]) for i in range(args.nbr_thread+1)]
    mail = (args.nbr_thread+1) * [0]

    liste_thread = [threading.Thread(target=transfer_message,
                                     args=[i+1,mail,lock,condition])
                                     for i in range(args.nbr_thread)]
    liste_thread.append(threading.Thread(target=initialisation_message,args=[0,mail,lock,condition]))
    liste_thread.append(threading.Thread(target=fin_message,args=[args.nbr_thread +1,mail,lock,condition]))
    
    for thread in liste_thread:
        thread.start()
    
    for thread in liste_thread:
        thread.join()