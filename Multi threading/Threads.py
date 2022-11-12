import threading
import time
import datetime

class Threads(threading.Thread):
    def __init__(self,name,time):
        threading.Thread.__init__(self)
        self.name=name
        self.time=time

    def run(self):
        lock.acquire()
        print(f"Entering {self.name}")
        now=datetime.datetime.now()
        for i in range(10):
            print(str(i)+"   "+now.strftime("%y-%m-%d %H-%M-%S"))
            time.sleep(self.time)
        print(f"Exiting {self.name}")
        lock.release()

lock=threading.Lock()
th_1=Threads("Thread 1",1)
th_2=Threads("Thread 2",0.5)
th_1.start()
th_2.start()
th_1.join()
th_2.join()