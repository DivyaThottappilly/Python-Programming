#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:15:08 2020

@author: divyathottappilly
"""
#Run time - O(n*W)
# A Dynamic Programming based Python Program for 0-1 Knapsack problem 
# Prints the maximum value and items of knapsack with W
def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    # stores the result of Knapsack 
    res = K[n][W] 
    print("Total value ",res) 
      
    w = W 
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
        # either the result comes from the 
        # top (K[i-1][w]) or from (val[i-1] 
        # + K[i-1] [w-wt[i-1]]) as in Knapsack 
        # table. If it comes from the latter 
        # one/ it means the item is included. 
        if res == K[i - 1][w]: 
            continue
        else: 
  
            # This item is included. 
            print("Item",i ,"with wt",wt[i - 1],"and value",val[i - 1]) 
              
            # Since this weight is included 
            # its value is deducted 
            res = res - val[i - 1] 
            w = w - wt[i - 1] 
# Driver program to test above function 
val = [60, 50, 70,30] 
wt = [5,3,4,2] 
W = 5
n = len(val) 
knapSack(W, wt, val, n)