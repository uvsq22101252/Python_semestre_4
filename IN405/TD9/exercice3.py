import threading
import argparse
from time import sleep
from random import randint

def sleep_time_barriere(nbr_th):
    for i in range(2):
        sleep(randint(1,5))
        print("le thread %s est reveillé"%(threading.get_ident()))
        lock.acquire()
        print("le thread %s vient d'etre mis en attente")
        nbr_th -=1
        if nbr_th ==0:
            print("les thread vont tous etre reveillés")
            nbr_th = args.nbr_thread
            condition.notify_all()
        else:
            condition.wait()
            print("le thread %s va etre notifier"%(threading.get_ident()))
        lock.release()



if __name__ == "__main__":
    argP = argparse.ArgumentParser()
    argP.add_argument("nbr_thread",type=int)
    args = argP.parse_args()

    lock= threading.Lock()
    condition = threading.Condition()
    liste_thread = [threading.Thread(target=sleep_time_barriere,args=[args.nbr_thread])for i in range(args.nbr_thread)]

    for elmt in liste_thread:
        elmt.start()
    
    for elmt in liste_thread:
        elmt.join()
