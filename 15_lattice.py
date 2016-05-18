# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:11:04 2016

@author: ORCHISAMA
"""
#Problem - 15
#lattice paths - find possible paths from upper left corner to bottom right corner in a nxn grid
#dynamic programming solution - for bottom nodes, there exists only 1 path.
#Path from any node is given as a sum of paths from the node to its right and the node to its bottom

N = 20
#creating a NxN matrix
path = [[0 for x in range(N+1)] for x in range(N+1)]

path[0][0] = 0
for i in range (1,N+1):
    path[0][i] = 1
    path[i][0] = 1
    
for i in range (1,N+1):
    for j in range(1,N+1):
        path[i][j] = path[i][j-1] + path[i-1][j]
        
print path[N][N]