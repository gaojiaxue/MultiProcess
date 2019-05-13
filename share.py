import multiprocessing as mp 
import time 

def job(v,num,l):
    l.acquire()
    for j in range(10):
        time.sleep(0.1)
        v.value+=num
        print(v.value)
    l.release()



def multicore():
    l=mp.Lock()
    v=mp.Value('i',0)
    p1=mp.Process(target=job,args=(v,1,l))
    p2=mp.Process(target=job,args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == "__main__":
    multicore()

# #share value 
# value=mp.Value('d',1)
# #share array
# array=mp.Array('i',[1,3,4])