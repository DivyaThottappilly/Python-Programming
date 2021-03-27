#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 08:57:52 2020

@author: divyathottappilly
"""

class Node:

    def __init__(self,key,data):
        self.left = None
        self.right = None
        self.key = key
        self.data = data

    def insert(self, key,data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(key,data)
                else:
                    self.left.insert(key,data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(key,data)
                else:
                    self.right.insert(key,data)
        else:
            self.key = key
            self.data = data
            
   # Print the tree
    def printInorder(self):
        if self.left:
            self.left.printInorder()
        print( self.key,self.data,),
        if self.right:
            self.right.printInorder()
            
# The function prints all the keys in the gicven range 
# [k1..k2]. Assumes that k1 < k2  
def printRange(root, k1, k2): 
      
    # Base Case 
    if root is None: 
        return 
  
    # Since the desired o/p is sorted, recurse for left 
    # subtree first. If root.data is greater than k1, then 
    # only we can get o/p keys in left subtree 
    if k1 < root.data : 
        printRange(root.left, k1, k2) 
  
    # If root's data lies in range, then prints root's data 
    if k1 <= root.data and k2 >= root.data: 
        print (root.data) 
  
    # If root.data is smaller than k2, then only we can get 
    # o/p keys in right subtree 
    if k2 > root.data: 
        printRange(root.right, k1, k2) 

# Use the insert method to add nodes
root = Node("abc",150)
root.insert("xyz",75)
root.insert("def",50)
root.insert("ghi",100)
root.insert("lmn",200)
root.insert("kyz",175)
root.insert("pqr",300)


root.printInorder()

printRange(root,175,300)