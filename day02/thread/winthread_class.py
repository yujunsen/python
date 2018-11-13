import threading
import time

mylock = threading.RLock()

class test(threading.Thread):
    def __init__(self, no, interval):
        """Constructor"""
        threading.Thread.__init__(self)
        self.no = no
        self.interval = interval
        self.isstop = False
    def run(self):
        while not self.isstop:
            mylock.acquire()
            self.no += 1
            mylock.release()
            print "thread id %d interval %d" %(self.interval, self.no)
            time.sleep(1)
    def setinterval(self, interval):
        self.interval = interval
    def stop(self):
        self.isstop = True
    
def factory():
    t1 = test(1,2)
    t1.start()
    t2 = test(2,2)
    t2.start()
    time.sleep(5)
    t1.setinterval(100)
    time.sleep(5)
    t1.stop()
    t2.stop()

if __name__ == "__main__":
    factory()
