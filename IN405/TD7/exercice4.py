import os 
import multiprocessing as mp
import argparse
import sys

def createID():
    return os.getpid()

def message(pipe_sortie):
    with os.fdopen(pipe_sortie, "w")as f :
        pid = createID()
        msg = "Hello you, my pid is %s" % (createID())
        print(pid, msg)
        f.write("%d\n%s\n" %(pid, msg))

def allgather(pipe_in,nb_process):
    dic = {}
    with os.fdopen(pipe_in)as f:
        for _ in range(nb_process):
            i = int(f.readline()[::-1])
            dic[i] = f.readline()[:-1]
    return dic


if __name__ == "__main__":
    
    AP = argparse.ArgumentParser()
    AP.add_argument("nbp", help="nombre de process voulu", type = int)
    args = AP.parse_args(sys.argv[1::])

    r, w = os.pipe()
    list_process = []

    for i in range(args.nbp):
        list_process.append(mp.Process(target=message, args=[w]))

    for p in list_process:
        p.start()

    os.close(w)
    dic = allgather(r, args.nbp)

    for key, value in dic.items():
        print("%d j'ai choisit '%s'." % (key, value))

    for p in list_process:
        p.join()