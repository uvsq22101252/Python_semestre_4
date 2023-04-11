import os
import multiprocessing as mp
import random


def hello_world(sortie):
    with open(sortie,"w") as f:
        f.write("Hello World")

def pair_int(sortie):
    with open(sortie,"w")as f:
        f.write("%d %d" %(random.randint(0,999), random.randint(0,999)))

path = "__pipe__"

if __name__ == "__main__":
    os.mkfifo(path)
    p1 = mp.Process(target=hello_world, args=[path])
    p1.start()
    with open(path) as b:
        print(b.read())
    p1.join()


    p2 = mp.Process(target=pair_int, args=[path])
    p2.start()
    with open(path) as b:
        pair = b.read()
        valeur_1= int(pair.split(" ")[0])
        valeur_2= int(pair.split(" ")[1])
    print("Valeur 1 : "+str(valeur_1)+"----"+"Valeur 2 : "+str(valeur_2))
    p2.join()