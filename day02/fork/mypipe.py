#!/usr/bin/env python
# coding=utf-8

import os
import time

def mypipe():
    a = 0
    r,w = os.pipe()
    pid = os.fork()
    if(pid == 0):
        os.close(r)
        w=os.fdopen(w,"w")
        print "this is child  %d" %(os.getpid())
        while a < 10:
            a = a + 1
            w.write(str(a))
            #print a
        w.close()
    else:
        print "this is parent %d" %(os.getpid())
        os.close(w)
        time.sleep(1)
        r = os.fdopen(r)
        print  r.read()
#        os.waitpid(pid, 0)
        r.close()

if __name__ == '__main__':
    mypipe()

