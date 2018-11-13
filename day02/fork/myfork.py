#!/usr/bin/env python
# coding=utf-8

import os
import time
def myfork():
    pid = os.fork()
    if pid == 0:
        time.sleep(1)
        print "\nthis is child  %d---%d\n" %(pid, os.getpid())
    else:
        print os.waitpid(pid, 0)    #子进程id status
        print "\nthis is parent %d---%d\n" %(pid, os.getpid())

if __name__ == '__main__':
    myfork()
