import os
import random
pid = os.fork()

if pid :
    os.wait()

    print("Hello World")
    print("Mon PID est "+ str(os.getpid()) + " et celui de mon fils est: "+str(pid))
else:
    print("Hello World")
    print("Mon PID est "+ str(pid)+ " et celui de mon père est:"+ str(os.getppid()))
    value = random.randint(0,10)
    print("la valeur aléatoire est: "+ str(value))