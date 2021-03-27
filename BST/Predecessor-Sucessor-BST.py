#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:58:05 2020

@author: divyathottappilly
"""
"""Input: root node, key
output: predecessor node, successor node

1. If root is NULL
      then return
2. if key is found then
    a. If its left subtree is not null
        Then predecessor will be the right most 
        child of left subtree or left child itself.
    b. If its right subtree is not null
        The successor will be the left most child 
        of right subtree or right child itself.
    return
3. If key is smaller then root node
        set the successor as root
        search recursively into left subtree
    else
        set the predecessor as root
        search recursively into right subtree"""

# Python program to find predecessor and successor in a BST
 
# A BST node
class Node: 
    # Constructor to create a new node
    def __init__(self, key):
        self.key  = key
        self.left = None
        self.right = None
 
# This function finds predecessor and successor of key in BST
# It sets pre and suc as predecessor and successor respectively
def findPreSuc(root, key):
    tmp = None
    # Base Case
    if root is None:
        return
 
    # If key is present at root
    if root.key == key:
        
        # the maximum value in left subtree is predecessor
        if root.left is not None:
            tmp = root.left 
            while(tmp.right):
                tmp = tmp.right 
            findPreSuc.pre = tmp
 
 
        # the minimum value in right subtree is successor
        if root.right is not None:
            tmp = root.right
            while(temp.left):
                tmp = tmp.left 
            findPreSuc.suc = tmp 
 
        return
 
    # If key is smaller than root's key, go to left subtree
    if root.key > key :
        findPreSuc.suc = root 
        findPreSuc(root.left, key)
 
    else: # go to right subtree
        findPreSuc.pre = root
        findPreSuc(root.right, key)
 
# A utility function to insert a new node in with given key in BST
def insert(node , key):
    if node is None:
        return Node(key)
 
    if key < node.key:
        node.left = insert(node.left, key)
 
    else:
        node.right = insert(node.right, key)
 
    return node
 
 
# Driver program to test above function
key = 65 #Key to be searched in BST
  
""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 
"""
root = None
root = insert(root, 50)
insert(root, 30);
insert(root, 20);
insert(root, 40);
insert(root, 70);
insert(root, 60);
insert(root, 80);
 
# Static variables of the function findPreSuc 
findPreSuc.pre = None
findPreSuc.suc = None
 
findPreSuc(root, key)
 
if findPreSuc.pre is not None:
    print( "Predecessor is", findPreSuc.pre.key)
 
else:
    print ("No Predecessor")
 
if findPreSuc.suc is not None:
    print ("Successor is", findPreSuc.suc.key)
else:
    print ("No Successor")