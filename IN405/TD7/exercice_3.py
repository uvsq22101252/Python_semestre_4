import os 
import multiprocessing as mp

def broadcast(pipe):
    with os.fdopen(pipe) as f:
        print("le PID du process est: %d, et il fournit comme message %s" % (os.getpid(),f.readline().split("\n")[0]))


nbr_process = 10

if __name__ == "__main__":
    list_process = []
    list_w = []
    for i in range (nbr_process):
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


