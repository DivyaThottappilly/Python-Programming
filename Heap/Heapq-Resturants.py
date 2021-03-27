#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 08:44:50 2020

@author: divyathottappilly
"""
import heapq as hq
import itertools 

#Extracting k nearby resturants 
#O(n) +O(klogn)

#pq = []                         # list of entries arranged in a heap
pq = [(500, 'resturant_1'), (1000, 'resturant_2'), (2000, 'resturant_3'), 
        (400, 'resturant_3'), (300, 'resturant_4'), (20, 'resturant_4')]

# Arrange based on distance can be done in O(n) 
hq.heapify(pq)

print("The Resturant list : ",end="") 
#Priority Queue 
print(pq)

#Extracting 3 can be done in O(klogn)
print("The 3 nearest resturants are : ",end="") 
print(hq.nsmallest(3, pq))


print("The 3 largest numbers in list are : ",end="") 
print(hq.nlargest(3, pq))


 
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    hq.heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = hq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')