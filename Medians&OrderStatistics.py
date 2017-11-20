#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:00:24 2017

@author: paulyang
"""
import random as rand
def minimum(nums):
    assert len(nums) > 0, 'list must be non empty'
    min_num = nums[0]
    for i in xrange(1, len(nums)):
        if min_num > nums[i]:
            min_num = nums[i]
    return min_num

def maximum(nums):
    assert len(nums) > 0, 'list must be non empty'
    max_num = nums[0]
    for i in xrange(1, len(nums)):
        if max_num < nums[i]:
            max_num = nums[i]
    return max_num

def minMax(nums):
    assert len(nums) > 0, 'list must be non empty'
    k = 0
    if len(nums) % 2 == 0:
        k = 2
        if nums[0] < nums[1]:
            min_num, max_num = nums[0], nums[1]
        else:
            min_num, max_num = nums[1], nums[0] 
    else:
        min_num = max_num = nums[0]
        k = 1
    for i in xrange(k, len(nums), 2):
        if nums[i] < nums[i + 1]:
            if min_num > nums[i]:
                min_num = nums[i]
            if max_num < nums[i + 1]:
                max_num = nums[i + 1]
        else:
            if min_num > nums[i + 1]:
                min_num = nums[i + 1]
            if max_num < nums[i]:
                max_num = nums[i]
    return min_num, max_num

def partition(nums, p, r):
    x = nums[r]
    i = p - 1
    for j in xrange(p, r):
        if nums[j] < x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[r] = nums[r], nums[i + 1]
    return i + 1

def randomPartition(nums, p, r):
    q = rand.randint(p, r)
    nums[q], nums[r] = nums[r], nums[q]
    return partition(nums, p, r)

# Time Complexity: O(n) in average, worst case: O(n^2)
# Auxiliary Space: O(1)
def randomizedSelect(nums, p, r, i):
    if p == r:
        return nums[r]
    q = randomPartition(nums, p, r)
    k = q - p + 1
    if i == k:
        return nums[q]
    elif i < k:
        return randomizedSelect(nums, p, q - 1, i)
    else:
        return randomizedSelect(nums, q + 1, r, i - k)
    
def randomizedSelectIterative(nums, p, r, i):
    while p != r:
        q = randomPartition(nums, p, r)
        k = q - p + 1
        if k == i:
            return nums[q]
        elif i < k:
            r = q - 1
        else:
            p = q + 1
            i -= k
    return nums[p]

def select(nums, p, r, i):
    if p == r:
        k = partition(nums, 0, len(nums) - 1) + 1
        if i == k:
            return nums[k-1]
        elif i < k:
            return select(nums[:k-1], 0, k-2, i)
        else:
            return select(nums[k:], 0, r-k, i-k)
    g_index = (r - p + 1) // 5
    median_indices = list()
    s = p
    for j in xrange(g_index):
        insertionSort(nums, s, s+4)
        median_indices.append(s+2)
        s += 5
    insertionSort(nums, s, r)
    median_indices.append((s+r)//2)
    for j in xrange(-1,-len(median_indices)-1,-1):
        nums[j], nums[median_indices[j]] = nums[median_indices[j]], nums[j]
    return select(nums, len(nums)-len(median_indices), len(nums)-1, i)

def insertionSort(nums, p, r):
    for i in xrange(p+1, r+1):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

arr = [2, 1, 3, 6, 4, 5, 7]
print select([2, 1, 3, 6, 4, 5, 7], 0, 6, 4)