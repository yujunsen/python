import threading
import time

class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在写代码%s' % threading.current_thread())  # threading.current_thread 当前线程id
            time.sleep(1)

class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在写画图%s' % threading.current_thread())  # threading.current_thread 当前线程id
            time.sleep(1)
def mian():
    t1 = CodingThread()
    t2 = DrawingThread()

    t1.start()
    t2.start()

if __name__ == '__main__':
    mian()