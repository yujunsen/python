import  time
import  threading

VALUE = 0

glock = threading.Lock()

def add_value():
    global  VALUE
    glock.acquire() #申请锁
    for x in range(10000000):
            VALUE += 1
    glock.release()#释放
    print(VALUE)


def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == '__main__':
    main()