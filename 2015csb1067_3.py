# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 09:53:30 2018

@author: nittin pc
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
random.seed(1)
G =  nx.read_edgelist("Wiki-Vote.txt",create_using=nx.DiGraph(), nodetype = int)
numNodes = G.number_of_nodes()
startNode = random.choice(list(G.nodes()))
#starting randomly from any node 
iterations = numNodes*1000
#higher the iterations higher is the agreement with the pagerank values as given by the default function
dict1 = {}
# dictionary containing the no of visits recorded after a random walk 
for i in list(G.nodes()):
    dict1[i] = 0
dict1[startNode] = dict1[startNode] + 1

currentNode = startNode
for i in range(0,iterations):
    #teleport in case the random no. is less than 0.2 or there is no next neighbour
    teleport = True if (random.random() < 0.2) else False
    noNext = True if (len(list(G.neighbors(currentNode))) == 0) else False
    if (teleport or noNext):
        nextNode = random.choice(list(G.nodes()))
        while(currentNode == nextNode):
            nextNode = random.choice(list(G.nodes()))
    #choosing randomly from the children of the node
    else:
        l = list(G.neighbors(currentNode))
        nextNode = l[random.randint(0,len(l)-1)]
    #adding the visits in the dictionary for each node    
    dict1[nextNode] = dict1[nextNode] + 1
    currentNode = nextNode
#plotting graph between the values given by no. of visits along x axis and nx.pagerank() values along y axis for corresponsding nodes     
ndlst = list(dict1.keys())
vstslst = [dict1[x] for x in ndlst]
pageRank = nx.pagerank(G) 
rankval = [10000*pageRank[x] for x in ndlst] 
plt.xlabel('No. of visits in Random Walk')
plt.ylabel('Value for node returned by nx.pagerank()')
plt.plot(vstslst,rankval,'r.')
#the correlation among the values of random walk with those assigned by pagerank is very large 
print('The Correlation Coefficient value for Number of visits and Pagerank values = ',np.corrcoef(vstslst,rankval)[0][1])
        
    
    