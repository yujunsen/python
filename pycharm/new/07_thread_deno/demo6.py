import threading
import time
from queue import  Queue

# q = Queue(4)
# q.put(1)
# q.put(2)
# #print(q.qsize())
# print(q.empty()) #死否未空

#q = Queue(4)

# for x in range(4):
#     q.put(x)
# #print(q.full()) #死否满
#
# for x in range(4):
#     print(q.get())
# #q.get(block=True) #get put 默认block=True

def set_value(q):
    index = 0
    while True:
        q.put(index)
        index += 1
        time.sleep(3)
def get_value(q):
    while True:
        print(q.get())
def main():
    q = Queue(4)
    q.put(1)
    #print(q.qsize())
    t1 = threading.Thread(target=set_value, args=[q])
    t2 = threading.Thread(target=get_value, args=[q])
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()