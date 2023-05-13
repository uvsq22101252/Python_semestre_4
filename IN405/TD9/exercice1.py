import threading
import argparse
import sys

lock = threading.Lock()

def count(compteur):
    for i in range(10):
        lock.acquire
        compteur[0] += 1
        lock.release


if __name__ == "__main__":
    argP = argparse.ArgumentParser()
    argP.add_argument("nbr_thread", type=int)
    args=argP.parse_args(sys.argv[1::])

    compteur = [0]
    liste_thread = [threading.Thread(target=count,args=[compteur])for i in range(args.nbr_thread)]

    for thread in liste_thread:
        thread.start()
    
    for thread in liste_thread:
        thread.join()

    print(compteur[0])

