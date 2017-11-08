#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:10:34 2017

@author: paulyang
"""

def countingSort(nums):
    # Ensure that nums are non negative
    assert min(nums) >= 0, 'Numbers in nums must be nonnegative.'
    # Find the maximum number in nums
    k = max(nums)
    # Initialize auxiliary list to store count of elements
    aux = [0] * (k + 1)
    # Initialize result list to store sorted nums
    # Index 0 stores nothing
    res = [0] * (len(nums) + 1)
    # Count number of elements in nums
    for num in nums:
        aux[num] += 1
    # Compute running sum of auxiliary list
    for i in range(1, len(aux)):
        aux[i] += aux[i - 1]
    # Place elements to result list
    for i in xrange(len(nums)-1, -1, -1):
        res[aux[nums[i]]] = nums[i]
        aux[nums[i]] -= 1
    return res[1:]