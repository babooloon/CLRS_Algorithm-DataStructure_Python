#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:55:05 2017

@author: paulyang
"""
#%% BST functions
class TreeNode():
    def __init__(self, key, p = None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.p = p
    
def inOrderTreeWalk(root):
    if root:
        inOrderTreeWalk(root.left)
        print root.key,
        inOrderTreeWalk(root.right)

def preOrderTreeWalk(root):
    if root:
        print root.key,
        preOrderTreeWalk(root.left)
        preOrderTreeWalk(root.right)

def postOrderTreeWalk(root):
    if root:
        postOrderTreeWalk(root.left)
        postOrderTreeWalk(root.right)
        print root.key,

def inOrderTreeWalkIterative(root):
    if root:
        stack = []
        curr = root
        while curr or stack:
            # Reach the leftmost node of current tree
            if curr:
                stack.append(curr)
                curr = curr.left
            # At this point, curr is None. If stack is not empty, then we backtrack
            # to top of stack
            elif stack:
                curr = stack.pop()
                print curr.key,
                curr = curr.right

# Use parent pointer, no recursion and no stack
def inOrderTreeWalkIterativeEnhanced(root):
    if root is not None:
        leftDone = False
        while root:
            # If left child is not traversed, then find the leftmost child
            if not leftDone:
                while root.left:
                    root = root.left
            # The leftmost child's left subtree is trivially done.
            # Print leftmost child's key
            print root.key,
            leftDone = True
            # If leftmost child has a right child, then move to its right child.
            if root.right:
                leftDone = False
                root = root.right
            # If leftmost child has no right child and it is not the root, then
            # backtrack using parent pointer to find its successor node.
            elif root.p:
                while root.p and root == root.p.right:
                    root = root.p
                if not root.p:
                    break
                root = root.p
            # If current node is root and has no right child, terminate.
            else:
                break

# Keep same key on the left subtree
# Time Complexity O(n)
def insertNode(root, node):
    assert root is not None, 'Root cannot be None'
    if node.key <= root.key:
        if root.left:
            insertNode(root.left, node)
        else:
            root.left = node
    else:
        if root.right:
            insertNode(root.right, node)
        else:
            root.right = node

# Call binarySearch before calling delete
def deleteNode(root, key):
    # always try to find the left adjacent element to substitute the root.
    pass
    
def treeSearch(root, key):
    if not root or root.key == key:
        return root
    if key <= root.key:
        return treeSearch(root.left, key)
    else:
        return treeSearch(root.right, key)

def treeSearchIterative(root, key):
    while root and root.key != key:
        if key <= root.key:
            root = root.left
        else:
            root = root.right
    return root

def treeMin(root):
    while root.left:
        root = root.left
    return root

def treeMax(root):
    while root.right:
        root = root.right
    return root

def treeMinRecursive(root):
    if not root.left:
        return root
    return treeMinRecursive(root.left)

def treeMaxRecursive(root):
    if not root.right:
        return root
    return treeMaxRecursive(root.right)

def treeSuccessor(root):
    if root.right:
        return treeMin(root.right)
    y = root.p
    while y and root == y.right:
        root = y
        y = y.p
    return y

def treePredecessor(root):
    if root.left:
        return treeMax(root.left)
    y = root.p
    while y and root == y.left:
        root = y
        y = y.p
    return y

#%% Initialization
five = TreeNode(5)
two = TreeNode(2)
nine = TreeNode(9)
one = TreeNode(1)
three = TreeNode(3)
seven = TreeNode(7)
thirteen = TreeNode(13)
four = TreeNode(4)
eight = TreeNode(8)
root = five
five.left = two
five.right = nine
two.left = one
two.right = three
nine.left = seven
nine.right = thirteen
three.right = four
seven.right = eight
two.p = five
nine.p = five
one.p = two
three.p = two
seven.p = nine
thirteen.p = nine
four.p = three
eight.p = seven
#%% test
print 'inorder tree walk iterative'
inOrderTreeWalkIterative(root)
print
print 'inorder tree walk iterative enhanced'
inOrderTreeWalkIterativeEnhanced(root)
print
print 'preorder tree walk'
preOrderTreeWalk(root)
print
print 'postorder tree walk'
postOrderTreeWalk(root)
print
print 'treeSearch with key 2'
print treeSearch(root, 2).key
print 'treeSuccessor of 8'
print treeSuccessor(eight).key
print 'treeSuccessor of 5'
print treeSuccessor(five).key
print 'treePredecessor of 7'
print treePredecessor(seven).key
print 'treePredecessor of 5'
print treePredecessor(five).key