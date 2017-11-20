#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:30:52 2017

@author: paulyang
"""

class Queue:
    def __init__(self):
        self.arr = [0] * 10
        self.head = 0
        self.tail = 0
    
    def enqueue(self, x):
        if self.size() == len(self.arr)-1:
            self.__growArray()
        self.arr[self.tail] = x
        self.tail += 1
        if self.tail == len(self.arr):
            self.tail = 0
        print 'head', self.head, 'tail', self.tail
    
    def dequeue(self):
        assert self.head != self.tail, 'underflow'
        x = self.arr[self.head]
        self.head += 1
        if self.head == len(self.arr):
            self.head = 0
        if self.size() == len(self.arr)//2-1:
            self.__shrinkArray()
        print 'head', self.head, 'tail', self.tail
        return x
    
    def size(self):
        return self.tail-self.head if self.tail>=self.head else self.tail-self.head+len(self.arr)
    
    def __growArray(self):
        size = len(self.arr)-1
        new_a = [0] * (2*len(self.arr))
        new_a[:len(self.arr)] = self.arr[self.head:] + self.arr[:self.head]
        self.arr = new_a
        self.head = 0
        self.tail = size
    
    def __shrinkArray(self):
        new_a = [0] * (len(self.arr)//2)
        new_a[:] = self.arr[self.head:self.tail+1] + self.arr[self.tail:self.head]
        self.arr = new_a
        self.head = 0
        self.tail = len(self.arr)-1
    
    def __repr__(self):
        return self.arr.__repr__()