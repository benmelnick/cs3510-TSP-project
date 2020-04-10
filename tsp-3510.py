import os
import sys
import math
from collections import defaultdict
import time

# check this out: https://en.wiipedia.org/wiki/Christofides_algorithm
class tsp:

    path = sys.argv[1]
    file = open(path, 'r')
    file = file.readlines()
    coord = []
    pd = set()
    visited = set()

    def pairwiseDistance(self):
        # start_time = time.time()
        self.getCoordinate()
        
        for a in self.coord:
            for b in self.coord:
                if a[0] != b[0] and (a[0], b[0]) not in self.visited and (b[0], a[0]) not in self.visited:
                	self.visited.add((a[0], b[0]))
                	dis = round(math.sqrt((a[2] - b[2])**2 + (a[1] - b[1])**2))
                	self.pd.add((a[0], b[0], dis))
        # end_time = time.time()
        print(self.pd)
        
        

    def getCoordinate(self):
        
        for line in self.file:
            temp = line.rstrip('\n').split()
            self.coord.append((int(temp[0]), float(temp[1]), float(temp[2])))
    

    def size(self):
        return len(self.file)

    #1. Create a minimum spanning tree T of G.
    class Graph:
        
        def __init__(self,vertices):
	        self.V= vertices
	        self.graph = []
          
   
        
        def addEdge(self,u,v,w):
            self.graph.append([u,v,w]) 
      
       
        def find(self, parent, i): 
            if parent[i] == i: 
                return i 
            return self.find(parent, parent[i]) 
      
        
        def union(self, parent, rank, x, y): 
            
        
        def KruskalMST(self): 
  
	# 2. Let O be the set of vertices with odd degree in T.
	# By the handshaking lemma, O has an even number of vertices.  

	#3.Find a minimum-weight perfect matching M in the induced
	#subgraph given by the vertices from O.

	#4. Combine the edges of M and T to form a connected multigraph H in which each vertex has even degree.
	#5. Form an Eulerian circuit in H.
	#6. Make the circuit found in previous step into a Hamiltonian circuit by skipping repeated vertices (shortcutting).
            
            
x = tsp()
x.pairwiseDistance()
