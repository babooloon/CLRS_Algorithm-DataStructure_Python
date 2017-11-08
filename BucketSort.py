#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:33:21 2017

@author: paulyang
"""
# Time Complexity: O(n)
# Space Auxiliary: O(n)
import math
import random as rand
def bucketSort(nums):
    assert min(nums) >= 0, 'nums must be greater than or equal to 0'
    assert max(nums) < 1, 'nums must be smaller than 1'
    n = len(nums)
    aux = list()
    for i in xrange(n):
        aux.append(list())
    for i in xrange(n):
        aux[int(math.floor(n*nums[i]))].append(nums[i])
    for i in xrange(n):
        insertionSort(aux[i])
    return [x for y in aux for x in y]

def insertionSort(nums):
    for j in xrange(1, len(nums)):
        key = nums[j]
        i = j - 1
        while i >= 0 and nums[i] > key:
            nums[i + 1] = nums[i]
            i -=1
        nums[i + 1] = key
nums = list()
for i in xrange(10):
    nums.append(rand.random())
print bucketSort(nums)