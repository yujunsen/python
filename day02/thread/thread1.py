#!/usr/bin/env python
# coding=utf-8

import thread
import time

def funt(no,a):
    print no
    #while True:
    #    a = a + 1
    #    print "Thread  no %d = %d," %(no, a)
    thread.exit_thread()
def test():
    thread.start_new_thread(funt,(1,2))
    thread.start_new_thread(funt,(2,2))

if __name__ == "__main__":
    test()
