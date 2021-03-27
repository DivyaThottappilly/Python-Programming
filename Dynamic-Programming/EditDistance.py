#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:40:22 2020

@author: divyathottappilly
"""
def editDistDP(str1, str2, m, n): 
    dp = [[-1]*(m + 1) for _ in range(n + 1)]
    return editDistDP_helper(str1, str2, m, n, dp)
 
def editDistDP_helper(str1, str2, m, n, dp):
    """If first string is empty, the only option is to 
    insert all characters of second string into first """
    if (m == 0): 
        return n
  
    """ If second string is empty, the only option is to 
    remove all characters of first string""" 
    if (n == 0): 
        return m
    
    """ if the recursive call has been 
    called previously, then return 
    the stored value that was calculated 
    previously """
    if (dp[m - 1][n - 1] != -1): 
        return dp[m - 1][n - 1] 
  
    """ If last characters of two strings are same, nothing 
    much to do. Ignore last characters and get count for 
    remaining strings. 
  
    Store the returned value at dp[m-1][n-1] 
    considering 1-based indexing """
  
    if (str1[m - 1] == str2[n - 1]):
        dp[m - 1][n - 1] = editDistDP_helper(str1, str2, m - 1, n - 1, dp) 
  
    """ If last characters are not same, consider all three 
    operations on last character of first string, recursively 
    compute minimum cost for all three operations and take 
    minimum of three values .Store the returned value at dp[m-1][n-1] 
    considering 1-based indexing """
    else:
        dp[m - 1][n - 1] = 1 + min(editDistDP_helper(str1, str2, m, n - 1, dp),  
                                      editDistDP_helper(str1, str2, m - 1, n, dp),  
                                      editDistDP_helper(str1, str2, m - 1, n - 1, dp) 
                                      )
    return dp[m-1][n-1]
 


# A Dynamic Programming based Python program for edit 
# distance problem 
def editDistDP(str1, str2, m, n): 
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m + 1): 
        for j in range(n + 1): 
  
            # If first string is empty, only option is to 
            # insert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    print('Cost of operation is :' + str(dp[m][n])) 
    i, j= m, n  
      
    while (i and j) : 
        if (str1[i - 1] == str2[j - 1]) : 
            i -= 1
            j -= 1
        elif(dp[i][j] == dp[i - 1][j - 1] + 1) : 
            print('Replaced '+str(str1[i-1])+' to '+str(str2[j-1]))
            i -= 1
            j -= 1  
        elif (dp[i][j] == dp[i - 1][j] + 1): 
            print('Deleted '+str(str1[i-1]))
            i -= 1
            
        elif (dp[i][j] == dp[i][j - 1] + 1): 
            print('Added '+str(str2[j-1]))
            j -= 1  
                
  
# Driver program 
str1 = "sunday"
str2 = "saturday"
  
editDistDP(str1, str2, len(str1), len(str2)) 