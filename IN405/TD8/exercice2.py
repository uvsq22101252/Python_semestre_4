import threading
import argparse
from random import randint
import sys

def somme(tableau,debut,fin,i,res):
    somme = 0
    for elmt in tableau[debut:fin]:
        somme += elmt
    res[i]=somme


def moyenne(tableau,debut,fin,i,res):
    sommem = 0
    for elmt in tableau[debut:fin]:
        sommem += elmt
    res[i] = sommem//len(tableau[debut:fin])

def minimum(tableau,debut,fin,i,res):
    res[i]=min(tableau[debut:fin])

def maximum(tableau,debut,fin,i,res):
    res[i]=max(tableau[debut:fin])

argP = argparse.ArgumentParser()

argP.add_argument("nbr_thread", type=int)
argP.add_argument("taille_tableau",type=int)
argP.add_argument("operation", choices=["+","/","M","m"])

operation = {
    "+":somme,
    "/":moyenne,
    "M":minimum,
    "m":maximum,
}

args = argP.parse_args(sys.argv[1::])

tableau = [randint(0,100) for i in range(args.taille_tableau)]
print(tableau)
res = args.nbr_thread * [0]
liste_thread = [threading.Thread(target=operation[args.operation],
                        args=(  tableau,
                                round(i*args.taille_tableau/args.nbr_thread),
                                round((i+1)*args.taille_tableau/args.nbr_thread),
                                i,
                                res))
            for i in range(args.nbr_thread)]

for thread in liste_thread:
    thread.start()

for thread in liste_thread:
    thread.join()

