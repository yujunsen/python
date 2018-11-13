#!/usr/bin/env python
# coding=utf-8

import os
import sys
import time

def myfork():
    if os.fork() > 0:
        print 1
        sys.exit(0)     
    os.setsid()#守护进程
    os.umask(0)

    pid = os.fork()
    if pid > 0: 
        sys.exit(0)

    a = 0

    fp = open("1.txt", "w")
    while a < 11:
        time.sleep(1)
        a = a+1
        fp.write(str(a))
        fp.write('\n')
        #print a
    fp.close()

if __name__ == "__main__":
    myfork()
