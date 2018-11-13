#!/usr/bin/env python
# coding=utf-8

import os 
import time
import signal

def onsignal_term(a,b):
    print 'over'

signal.signal(signal.SIGTERM, onsignal_term)

def myfork():
    pid = os.fork()
    if pid == 0:
        a = 0
        while True:
            a = a +1
            print a
            time.sleep(1)
            if a > 10:
                os.kill(os.getppid(), signal.SIGTERM)
    else:
        os.waitpid(pid, 0)

if __name__ == "__main__":
    myfork()
