import threading
from random import randint
value = randint(0,999)
def hello():
    print("Salut bande de ...")

def num_alea():
    global value
    print("jai choisit: "+str(value))
    return value


if __name__ == "__main__":
    value = 0
    t1 = threading.Thread(target=hello)
    t1.start()
    t1.join()
    t2 = threading.Thread(target=num_alea)
    t2.start()
    print(type(t2.join()))
    print("le nombre choisit par le thread est :%d" %(value))
