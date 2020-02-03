#!/usr/bin/env python
# coding: utf-8

# Implementing heaps 

# In[37]:


#imports
from collections import defaultdict
from typing import List, Dict
import pprint
import networkx as nx
import matplotlib.pyplot as plt
from math import floor
from math import inf


# In[38]:


class MyHeapMax():
    """Maintain a balanced binary tree where locally parent's value >= either of its children's value
    """
    def __init__(self, inputlist: List[int]):
        """
        creates a heap with entries in inputlist
        """
        self.numberofnodes = len(inputlist)
        self.memberlist = inputlist
        self.heapify_naive()

        
    def heapify_naive(self):
        self.memberlist.sort(reverse = True)
        
    def height(self):
        """returns height of the heap"""
        #if heap has only 1 = (binary 1) node, it has height 1
        #if heap has 2 (binary 10) or 3 (binary 11) nodes, it has height 2
        #if heap has n nodes, it has height (number of digits of n in binary rep)
        #bin(n) = "0b" + binaryrep of n as a string
        return len(bin(self.numberofnodes)) - 2
    
    #numbering of nodes starts from 0 (root node)
    #leftchild of node number i is node number 2i+1
    #rightchild of node number i is node number 2i+2
    #parent of node number j = 2i+1 or 2i+2 is i = floor((j-1)/2) 
    
    def repair_up(self, pos_of_val: int, val: int):
        """
        repair the heap by moving up from val = value at pos_of_val till root node (if needed)
        """
        while pos_of_val >= 1:
            pos_of_parent = (pos_of_val -1)//2 #this is floor((pos_of_val -1)/2)
            val_of_parent = self.memberlist[pos_of_parent]
            #repair parent value
            if val_of_parent < val:
                #switch val and val_of_parent
                self.memberlist[pos_of_val] = val_of_parent
                self.memberlist[pos_of_parent] = val
                pos_of_val = pos_of_parent
            else:
                break
                
    def repair_down(self, pos_of_val: int, val: int):
        """
        repair the heap by moving down from val = value at pos_of_val till leaf (if needed)
        """
        #pos_of_val is a leaf if 2*pos_of_val + 1 > number of nodes -1 
        while (pos_of_val < self.numberofnodes) and (2*pos_of_val < self.numberofnodes - 1) :
                    pos_of_left_child = 2*pos_of_val+1
                    pos_of_right_child = 2*pos_of_val+2
                    val_of_left_child = self.memberlist[pos_of_left_child]
                    if pos_of_right_child < self.numberofnodes:
                        val_of_right_child = self.memberlist[pos_of_right_child]
                    else:
                        val_of_right_child = -1*inf
                    childrenlist = [(pos_of_left_child, val_of_left_child), (pos_of_right_child, val_of_right_child)]
                    pos_of_max_child, val_of_max_child = max(childrenlist, key = lambda x: x[1])
                    #swap val with max of its children if val < both its children
                    if val < val_of_max_child:
                        #switch val and val_of_max_child
                        self.memberlist[pos_of_val] = val_of_max_child
                        self.memberlist[pos_of_max_child] = val
                        pos_of_val = pos_of_max_child
                    else:
                        break
  
    def insert_value(self, val: int):
        """
        inserts val into heap
        """
        self.numberofnodes += 1
        
        #insert val in at the end
        self.memberlist.append(val)
        pos_of_val = self.numberofnodes - 1
        
        #repair the heap by moving up from val till root node (if needed)
        self.repair_up(pos_of_val, val)
    
        
        
    def delete_max(self)-> int:
        """
        deletes the maximum entry from the heap and returns it
        """

        if self.numberofnodes == 0:
            print("Already empty heap")
            return None        
        
        max_val = self.memberlist[0]
        self.numberofnodes -= 1
        
        if self.numberofnodes == 0:
            print("Heap is empty now")
            self.memberlist = []
            return max_val
        
        
        #deletes the last node value
        homeless_val = self.memberlist.pop(-1)
        #insert it at the top of the heap
        self.memberlist[0] = homeless_val
        
        
        #repair the heap by moving down from val till leaf (if needed)
        pos_of_homeless_val = 0
        self.repair_down(pos_of_homeless_val, homeless_val)
        return max_val
    
    
    def update_at(self, pos_of_val: int, new_val: int):
        """
        Updates the heap by replacing the old_val in node at position "pos" with new_val
        """

        if (pos_of_val < 0) or (pos_of_val >= self.numberofnodes):
            print("Invalid position")
            return
        
        if new_val == self.memberlist[pos_of_val]:
            print("Same value!")
            return
        
        if new_val > self.memberlist[pos_of_val]:
            #insert it at pos
            self.memberlist[pos_of_val] = new_val
            #repair the heap by moving up from val till root node (if needed)
            self.repair_up(pos_of_val, new_val)
           
            
            
        if new_val < self.memberlist[pos_of_val]:
            #insert it at pos
            self.memberlist[pos_of_val] = new_val
            #repair the heap by moving down from val till leaf (if needed)  
            self.repair_down(pos_of_val, new_val)
                
        print(self.memberlist)
    
        
        
        
        


# In[49]:


aheap = MyHeapMax([10,8,77,6,33,2])


# In[50]:


aheap.memberlist


# In[51]:


aheap.insert_value(20)


# In[52]:


aheap.memberlist


# In[53]:


aheap.delete_max()


# In[54]:


aheap.memberlist


# In[55]:


aheap.update_at(2, 77)


# In[56]:


aheap.update_at(1, 0)


# In[57]:


aheap.delete_max()


# In[59]:


aheap.delete_max()


# In[60]:


aheap.memberlist


# In[ ]:




