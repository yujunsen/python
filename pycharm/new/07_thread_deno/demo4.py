import threading
import time
import random


glock = threading.Lock()

gMoney = 1000
gTotalTimes = 10
gTimes = 0

class Producer(threading.Thread):
    def run(self):
        global  gMoney
        global  gTimes
        while True:
            money = random.randint(100, 1000)
            glock.acquire()
            if gTimes >= gTotalTimes:
                glock.release()
                break
            gTimes += 1
            gMoney += money
            print('%s 生产了%d元 剩余%d元' %(threading.current_thread(), money, gMoney))
            glock.release()
            # if gTimes >= gTotalTimes:
            #     break
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global  gMoney
        while True:
            money = random.randint(100, 1000)
            glock.acquire()
            if gMoney >= money:
                gMoney -= money
                print('%s消费者 消费了%d元，剩余%d元' %(threading.current_thread(), money, gMoney))
            else :
                if gTimes >= gTotalTimes:
                    glock.release()
                    break
                print('%s消费者消费%d元, 总共%d元, 不足%d元' %(threading.current_thread(), money, gMoney, money - gMoney))
            glock.release()
            time.sleep(0.5)


def main():
    for x in range(5):
        t = Producer(name='生产者线程%d' %x)
        t.start()
    for x in range(3):
        t = Consumer(name='消费线程%d' %x)
        t.start()


if __name__ == '__main__':
    main()