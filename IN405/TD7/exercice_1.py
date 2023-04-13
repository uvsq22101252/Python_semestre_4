import os
import multiprocessing as mp
import random


def hello_world(sortie):
    os.close(r)
    with os.fdopen(sortie,"w") as f:
        f.write("Hello World")

def pair_int(sortie):
    os.close(r)
    with os.fdopen(sortie,"w")as f:
        f.write("%d %d" %(random.randint(0,999), random.randint(0,999)))


if __name__ == "__main__":
    r,w = os.pipe()
    p1 = mp.Process(target=hello_world, args=[w])
    p1.start()
    os.close(w)
    with os.fdopen(r) as b:
        print(b.read())
    p1.join()


    r,w = os.pipe()
    p2 = mp.Process(target=pair_int, args=[w])
    p2.start()
    os.close(w)
    with os.fdopen(r) as b:
        pair = b.read()
        valeur_1= int(pair.split(" ")[0])
        valeur_2= int(pair.split(" ")[1])
        print("Valeur 1 : "+str(valeur_1)+"----"+"Valeur 2 : "+str(valeur_2))
    p2.join()