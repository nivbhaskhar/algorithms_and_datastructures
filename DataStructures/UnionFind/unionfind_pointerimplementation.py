import random
from typing import List
from collections import defaultdict, Counter

class unionfind:
    def __init__(self, n: int):
        d= {}
        for i in range(1,n+1):
            d[i] = i

        self.my_rep = d    

    def find(self, i: int)-> int:
        temp_rep = self.my_rep[i]
        if i == temp_rep:
           return i
            
        current_rep = self.find(temp_rep)
        self.my_rep[i] = current_rep
        return current_rep

    def union(self, i: int, j:int):
        rep_i = self.find(i)
        rep_j = self.find(j)
        if random.randint(0,1):
            self.my_rep[rep_i] = rep_j
        else:
            self.my_rep[rep_j] = rep_i
        
        
        
