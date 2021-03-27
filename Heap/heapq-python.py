#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:26:54 2020

@author: divyathottappilly
"""
import heapq
def heapsort(iterable):
   h = []
   for value in iterable:
      heapq.heappush(h, value)
   return [heapq.heappop(h) for i in range(len(h))]
print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

# initializing list 
li = [5, 7, 9, 1, 3]   
# using heapify to convert list into heap 
heapq.heapify(li)
print(li)
heapq.heappush(li,4) 
print(li)

print("The 3 largest numbers in list are : ",end="") 
print(heapq.nlargest(3, li))

print("The 3 smallest numbers in list are : ",end="") 
print(heapq.nsmallest(3, li))

# import modules 
import heapq as hq 
  
# list of students 
list_stu = [(5,'Rina'),(1,'Anish'),(3,'Moana'),(2,'cathy'),(4,'Lucy')]   
# Arrange based on the roll number 
hq.heapify(list_stu)   
print("The order of presentation is :") 
  
for i in list_stu: 
  print(i[0],':',i[1])