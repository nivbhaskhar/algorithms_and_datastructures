#Dijkstra without heaps


# Input

# V is a set of vertices
# A adj_dict is the adjacency dictionary, where A[v] = [(w, wt of edge v-w) for w nbhr of v]
# s = source vertex
# t = target vertex

import math
import pprint

def shortest_path(V, A, s, t):
    potential_burn_times = {}
    for v in V:
        potential_burn_times[v] = math.inf
        
    potential_burn_times[s] = 0

    def find_and_remove_min():
        min_time = math.inf
        to_be_burnt_vertex = None
        for v in potential_burn_times:
            if min_time > potential_burn_times[v]:
                min_time = potential_burn_times[v]
                to_be_burnt_vertex = v
        if to_be_burnt_vertex is not None:
            del potential_burn_times[to_be_burnt_vertex]

        return min_time, to_be_burnt_vertex

    
    last_burn_time = None
    burnt_vertices = {}
    while (last_burn_time != math.inf):
        burning_time, to_be_burnt_vertex = find_and_remove_min()
        if to_be_burnt_vertex is not None:
            #burn the to_be_burnt_vertex, update last_burn_time
            burnt_vertices[to_be_burnt_vertex] = burning_time
            last_burn_time = burning_time
            #Update potential burning times of nbhrs of burnt vertex
            for nbhr, edge_wt in A[to_be_burnt_vertex]:
                if nbhr in potential_burn_times:
                    potential_burn_times[nbhr] = min(potential_burn_times[nbhr],last_burn_time+edge_wt)

        else:
            last_burn_time = math.inf
            
    pprint.pprint(burnt_vertices)
    if t in burnt_vertices:
        return burnt_vertices[t]
    else:
        return 'Unreachable'
            
                

V = {'A', 'B', 'C', 'D', 'E','L','I'}
A = {'A': [('B',3), ('C', 1)] ,
     'B': [('A',3), ('C',7), ('D',5), ('E',1)] ,
     'C': [('B',7), ('A',1), ('D',2)],
     'D': [('B',5), ('C',2), ('E',7)] ,
     'E': [('B',1), ('D',7)],
     'L' : [('I',1)],
      'I': [('L', 1)]}
print(shortest_path(V, A, 'C', 'E'))   
        
    
    
        

