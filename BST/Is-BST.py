#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:54:34 2020

@author: divyathottappilly
"""
#Time Complexity: O(n)
#Auxiliary Space : O(1) if Function Call Stack size is not considered, otherwise O(n)
# Python program to check if a binary tree is bst or not 
  
INT_MAX = 4294967296
INT_MIN = -4294967296
  
# A binary tree node 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
  
# Returns true if the given tree is a binary search tree 
# (efficient version) 
def isBST(node): 
    return (isBSTUtil(node, INT_MIN, INT_MAX)) 
  
# Retusn true if the given tree is a BST and its values 
# >= min and <= max 
def isBSTUtil(node, mini, maxi): 
      
    # An empty tree is BST 
    if node is None: 
        return True
  
    # False if this node violates min/max constraint 
    if node.data < mini or node.data > maxi: 
        return False
  
    # Otherwise check the subtrees recursively 
    # tightening the min or max constraint 
    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, maxi)) 

"""
Time Complexity: O(n)
We can avoid the use of Auxiliary Array. 
While doing In-Order traversal, we can keep track of 
previously visited node. If the value of the currently 
visited node is less than the previous value,
then tree is not BST. Thanks to ygos for this space optimization.
global variable prev - to keep track 
of previous node during Inorder  
#traversal """
prev = None
  
# function to check if given binary 
# tree is BST 
def isbst(root): 
      
    # prev is a global variable 
    global prev 
    prev = None
    return isbst_rec(root) 
  
  
# Helper function to test if binary 
# tree is BST 
# Traverse the tree in inorder fashion  
# and keep track of previous node 
# return true if tree is Binary  
# search tree otherwise false 
def isbst_rec(root): 
      
    # prev is a global variable 
    global prev  
  
    # if tree is empty return true 
    if root is None: 
        return True
  
    if isbst_rec(root.left) is False: 
        return False
  
    # if previous node'data is found  
    # greater than the current node's 
    # data return fals 
    if prev is not None and prev.data > root.data: 
        return False
  
    # store the current node in prev 
    prev = root 
    return isbst_rec(root.right) 

# Compute the "maxDepth" of a tree -- the number of nodes  
# along the longest path from the root node down to the  
# farthest leaf node 
#Time Complexity: O(n) 
def maxDepth(node): 
    if node is None: 
        return 0 ;  
    else : 
        # Compute the depth of each subtree 
        lDepth = maxDepth(node.left) 
        rDepth = maxDepth(node.right) 
        # Use the larger one 
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1
# driver code to test above function 
root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
  
if isbst(root): 
    print("is BST") 
else: 
    print("not a BST") 
  

  
# Driver program to test above function 
root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
  
if (isBST(root)): 
    print ("Is BST")
else: 
    print ("Not a BST")
    
print ("Height of tree is %d" %(maxDepth(root))) 