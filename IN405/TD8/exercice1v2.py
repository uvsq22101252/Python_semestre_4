import threading
import random
import queue

def hello():
    print("Hello world")

def printnumber(number):
    print("process princicpale a généré "+str(number))

def gen_number():
    galea = random.randint(0,100)
    print("le process fils a généré " +str(galea))
    queue.put(galea)

def moyenne(n):
    moyenne = sum(n)//len(n)
    print("la moyenne est de "+str(moyenne))


if __name__ == "__main__":
    alea = random.randint(0,100)
    chiffre = [random.randint(0,100) for i in range(0,10)]
    queue = queue.Queue()

    Th= [  
        threading.Thread(target=hello),
        threading.Thread(target=printnumber, args=[alea]),
        threading.Thread(target=gen_number),
        threading.Thread(target=moyenne,args=[chiffre])

    ]    
   
    for thread in Th:
        thread.start()
    
    for thread in Th:
        thread.join()

    print("J'ai recupéré le nombre générer par le processus fils " +str(queue.get()))