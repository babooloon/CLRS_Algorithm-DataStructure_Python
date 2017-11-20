#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:03:34 2017

@author: paulyang
"""
import copy

MIN_SIZE = 10
class Stack:
    def __init__(self):
        self.arr = [0] * MIN_SIZE
        self.top = -1

    def empty(self):
        return True if self.top == -1 else False
    
    def push(self, x):
        self.top += 1
        if self.top == len(self.arr):
            self.__growArray()
        self.arr[self.top] = x
    
    def pop(self):
        assert not self.empty(), 'underflow'
        x = self.arr[self.top]
        if self.top == len(self.arr)//2 and len(self.arr) > MIN_SIZE:
            self.__shrinkArray()
        self.top -= 1
        return x
    
    def __growArray(self):
        print 'grow array'
        new_a = [0] * (2 * len(self.arr))
        new_a[:len(self.arr)] = copy.deepcopy(self.arr)
        self.arr = new_a
    
    def __shrinkArray(self):
        print 'shrink array'
        new_a = [0] * (len(self.arr)//2)
        new_a = copy.deepcopy(self.arr[:self.top])
        self.arr = new_a
    
    def __repr__(self):
        return self.arr.__repr__()