#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:42:50 2017

@author: paulyang
"""
class Node:
    def __init__(self, key=None):
        self.pre = None
        self.next = None
        self.key = key
    
    def __repr__(self):
        return str(self.key)

class LinkedList:
    def __init__(self):
        self.nil = Node()
        self.nil.next = self.nil
        self.nil.pre = self.nil
    
    def listSearch(self, k):
        self.nil.key = k
        x = self.nil.next
        while x.key != k:
            x = x.next
        return x if x != self.nil else None
    
    def listInsert(self, n):
        n.next = self.nil.next
        self.nil.next.pre = n
        self.nil.next = n
        n.pre = self.nil
    
    def listDelete(self, n):
        n.next.pre = n.pre
        n.pre.next = n.next
    
    def __repr__(self):
        rep = list()
        n = self.nil.next
        while n != self.nil:
            rep.append(n.key)
            n = n.next
        rep = map(str, rep)
        return '-'.join(rep)
    
ll = LinkedList()
ll.listInsert(Node(1))
ll.listInsert(Node(4))
ll.listInsert(Node(16))
ll.listInsert(Node(9))
print ll
ll.listDelete(ll.listSearch(4))
print ll
ll.listDelete(ll.listSearch(1))
print ll
ll.listDelete(ll.listSearch(9))
print ll
ll.listDelete(ll.listSearch(16))
print ll
print ll.listSearch(7)