#!/usr/bin/env python
# coding=utf-8

"""
def f1():
    print 9
#f1()

def f2(a):
    print a

b = ("dsadas", 12, "asd", 2.4)

for a in b:
    f2(a)
"""

def f3(a=1, b=2, c=3):
    print 'a', a
    print 'b', b
    print 'c = %d' %c
    return a, a+b

d=f3(b=4,c=3)
#print c
print d
