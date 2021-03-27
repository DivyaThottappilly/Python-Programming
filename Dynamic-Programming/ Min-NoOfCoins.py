#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:10:53 2020

@author: divyathottappilly
"""

INF = 100000

#k is number of denominations of the coin or length of d
def coin_change_modified(d, n, k):
  M = [0]*(n+1)
  S = [0]*(n+1)

  for j in range(1, n+1):
    minimum = INF
    coin = 0

    for i in range(1, k+1):
      if(j >= d[i]):
        minimum = min(minimum, 1+M[j-d[i]])
        coin = i
    M[j] = minimum
    #print(str(M[j]))
    S[j] = coin
    #print(str(S[j]))

  l = n
  while(l>0):
    print(d[S[l]])
    l = l-d[S[l]]
  return M[n]

if __name__ == '__main__':
  # array starting from 1, element at index 0 is fake
  d = [0, 1, 2, 3]
  coin_change_modified(d, 5, 3) #to make 5. Number of denominations = 3