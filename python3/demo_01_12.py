#!/usr/bin/env python
# coding=utf-8

import time

def tail(f):
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(1)
            continue;
        yield line

if __name__ == "__main__":
    f = open("1.txt")
    tail(f)
    f.close()
