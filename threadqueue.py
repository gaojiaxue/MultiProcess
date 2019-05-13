import threading
import time 
from queue import Queue

def job(l,q):
    for i in range(len(l)):
        l[i]=l[i]**2
    q.put(l)

def multithreading(data):
    q=Queue()
    threads=[]
    for i in range(4):
        t=threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results=[]
    for j in range(4):
        results.append(q.get())
    print(results) 

def normal(l):
    for i in range(len(l)):
        l[i]=l[i]**2
    return l


if __name__ == "__main__":
    data1=[[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    data2=[[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    st=time.time()
    multithreading(data1)
    st1=time.time()
    print('multithread time:',st1-st)
    res=[]
    for x in range(4):
        res.append(normal(data2[x]))
    print(res)
    st2=time.time()
    print('normal time:',st2-st)
    
    