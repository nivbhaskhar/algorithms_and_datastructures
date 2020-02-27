"""
https://leetcode.com/discuss/interview-question/356981


Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. The i-th edge connects nodes edges[i][0] and edges[i][1] together. Your task is to augment this set of edges with additional edges to connect all the nodes. Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each other.

Input:

n, an int representing the total number of nodes.
edges, a list of integer pair representing the nodes already connected by an edge.
newEdges, a list where each element is a triplet representing the pair of nodes between which an edge can be added and the cost of addition, respectively (e.g. [1, 2, 5] means to add an edge between node 1 and 2, the cost would be 5).
Example 1:

Input: n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
Output: 7
Explanation:
There are 3 connected components [1, 4, 5], [2, 3] and [6].
We can connect these components into a single component by connecting node 1 to node 2 and node 1 to node 6 at a minimum cost of 5 + 2 = 7.


"""

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
        
        
        


class Solution:


        
    def mincost(self, n: int, edges: List[List[int]], newEdges: List[List[int]]) -> int:
        
        for edge in edges:
            newEdges.append([edge[0], edge[1], 0])
        newEdges.sort(key = lambda x: x[2])
        weightofspanningtree = 0


        connectedcomponents = unionfind(n)
        for edge in newEdges:
            c0 = connectedcomponents.find(edge[0])
            c1 = connectedcomponents.find(edge[1])
            if c0 != c1:
                weightofspanningtree += edge[2]
                connectedcomponents.union(c0, c1)
        return weightofspanningtree        
            


            
            
        
    




solution = Solution()
print(solution.mincost(6, [[1, 4], [4, 5], [2, 3]],[[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]))

