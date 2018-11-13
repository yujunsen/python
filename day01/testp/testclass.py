#!/usr/bin/env python
# coding=utf-8


class a:
    def __init__(self):
        """aaaa"""
        self.m = 1
    def add(self):
        """dddd"""
        self.p=4
        print self.p + self.m

class b(a):
    def __init__(self):
        """ssss"""
        a.__init__(self)
        self.n = 2
    def sum(self):
        """zzzz"""
        print self.m + self.n
    def __dd(self):	#__ == private
    	print "ddddd"
    def getdd(self):
    	self.__dd()
    	try:
    		func()
    	except Exception, e:
    		print e.message
    def funx():
    	pass #占位符
c=b()
c.sum()
c.add()
c.getdd()
print 31231231
