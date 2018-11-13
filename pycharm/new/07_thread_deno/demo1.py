import threading
import time

# def coding():
#     for x in range(3):
#         print('正在写代码%s' %x)
#         time.sleep(1)
# def drawing():
#     for x in range(3):
#         print('正在写画图%s' %x)
#         time.sleep(1)
#
# def main():
#     coding()
#     drawing()
#
# if __name__ == '__main__':
#     main()

def coding():
    for x in range(3):
        print('正在写代码%s' %threading.current_thread()) #threading.current_thread 当前线程id
        time.sleep(1)
def drawing():
    for x in range(3):
        print('正在写画图%s' %threading.current_thread())
        time.sleep(1)

def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)
    t1.start()
    t2.start()

    print('线程%s' %threading.enumerate())

if __name__ == '__main__':
    main()