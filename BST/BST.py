#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:17:40 2020

@author: divyathottappilly
"""



class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
   # findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
            
   # Print the tree
    def printInorder(self):
        if self.left:
            self.left.printInorder()
        print( self.data),
        if self.right:
            self.right.printInorder()
            
    # Print the tree
    def printPostorder(self):
        if self.left:
            self.left.printPostorder()
        if self.right:
            self.right.printPostorder() 
        print( self.data)    
  
  
    # Print the tree
    def printPreorder(self):
        print( self.data)   
        if self.left:
            self.left.printPreorder()
        if self.right:
            self.right.printPreorder() 
        
  
  

        

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.printInorder()
root.printPostorder()
root.printPreorder()

print(root.findval(7))
print(root.findval(6))