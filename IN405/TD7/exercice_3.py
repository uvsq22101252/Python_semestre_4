import os 
import multiprocessing as mp
import argparse
import sys

def broadcast(pipe):
    with os.fdopen(pipe) as f:
        print("le PID du process est: %d, et il fournit comme message %s" % (os.getpid(),f.readline().split("\n")[0]))




if __name__ == "__main__":
    
    AP = argparse.ArgumentParser()
    AP.add_argument("nbp", help="nombre de process voulu", type = int)
    args = AP.parse_args(sys.argv[1::])


    list_process = []
    list_w = []
    for i in range (args.nbp):
        r, w = os.pipe()
        list_w.append(w)
        list_process.append(mp.Process(target=broadcast, args=[r]))
    
    for p in list_process:
        p.start()
    
    for w in list_w :
        with os.fdopen(w,"w") as f:
            f.write("Good morning Sir\n")
    
    for p in list_process:
        p.join()


