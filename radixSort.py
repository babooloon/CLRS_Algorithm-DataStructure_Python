#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:53:48 2017

@author: paulyang
"""
# Time Complexity: O(d(n + k)), where d = L, n is the number of elements, k is
# the number of values each digit can take. Assume d is rather small so that
# len() and str() take O(1) time.
# Auxiliary Space: O(nd)
def radixSort(nums):
    # Ensure all nums are nonnegative
    if not nums:
        return nums
    assert min(nums) >= 0, 'All numbers must be nonnegative'
    # Convert all nums to strings and prepend 0 to ensure all nums have same
    # number of digits
    L = max(map(lambda x: len(str(x)), nums))
    numstrs = map(lambda x: '0'*(L-len(str(x)))+str(x), nums)
    # Sort nums from least significant digit to most significant digit by 
    # couting sort
    for i in xrange(L-1, -1, -1):
        numstrs = modifiedCountingSort(numstrs, i)
    return map(int, numstrs)
def modifiedCountingSort(numstrs, i):
    digits = map(lambda x: int(x[i]), numstrs)
    aux = [0] * 10
    res = [0] * (len(numstrs) + 1)
    for d in digits:
        aux[d] += 1
    for i in xrange(1, len(aux)):
        aux[i] += aux[i - 1]
    for i in xrange(len(digits)-1, -1, -1):
        res[aux[digits[i]]] = numstrs[i]
        aux[digits[i]] -= 1
    return res[1:]
print radixSort([329, 457, 657, 839, 436, 720, 355])

def radixSortWords(words):
    if not words:
        return words
    # Ensure all words have the same length
    assert all(map(lambda x: len(x)==len(words[0]), words)), 'All words must have same length.'
    for i in xrange(len(words[0])-1, -1, -1):
        words = modifiedCountingSortWords(words, i)
    return words
def modifiedCountingSortWords(words, i):
    chars = map(lambda x: ord(x[i])-ord('A'), words)
    aux = [0] * 26
    res = [0] * (len(words) + 1)
    for c in chars:
        aux[c] += 1
    for i in xrange(1, len(aux)):
        aux[i] += aux[i - 1]
    for i in xrange(len(chars)-1, -1, -1):
        res[aux[chars[i]]] = words[i]
        aux[chars[i]] -= 1
    return res[1:]
print radixSortWords(['COW','DOG', 'SEA', 'RUG', 'ROW', 'MOB', 'BOX', 'TAB', 'BAR', 'EAR', 'TAR', 'DIG', 'BIG', 'TEA', 'NOW', 'FOX'])