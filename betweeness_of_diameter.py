# -*- coding: utf-8 -*-
"""

@author: Vishal Singh(2015csb1040), Sonu(2015csb1034) 
"""

"""
the blue histogram showsthe distribution of edges with different 
edge betweenness centralities.The maximum number of edges are with
 the centrality between 0.003 to 0.005. There are very less edges with
 high centrality and these edges are the weak ties. Now we have plotted 
 with the red line the edge centrality of the longest shortest path(diameter).
These edges lie in the high centrality region.
Observation: the diameter of the connected graph comprises of weak ties. 
"""

import numpy as np
from scipy.stats import gaussian_kde
import networkx as nx;
import matplotlib.pyplot as plt;
def longest_friendship():

    

    G = nx.read_adjlist('pagerank.txt',nodetype = int,create_using = nx.DiGraph())
    
    max_min_distance = -1
    graph_nodes = G.nodes();
    n1 = 0
    n2 = 0
    for node1 in graph_nodes:
        for node2 in graph_nodes:
            #print(node1,node2)
            try: 
                distance = nx.shortest_path_length(G,source= node1,target = node2)
                #print(distance)
            except NetworkXNoPath:
                    print("No Path exists between Node",node1,"and",node2)
            else :
            
                    if (max_min_distance <= distance):
                        max_min_distance = distance
                        n1 = node1
                        n2 = node2
                        
    print("Source =",n1,"Target =", n2 , "Distance/Hops =",max_min_distance)
    pos = nx.spring_layout(G)
    # draw path in red
    path = nx.shortest_path(G,source=n1,target=n2)
    return path
G = nx.read_adjlist('pagerank.txt',nodetype = int,create_using = nx.DiGraph())
centralities= []
centralities.append(nx.edge_betweenness_centrality(G))
lists = sorted(centralities[0].items())
plt.hist([i[1] for i in lists[:]])
path=longest_friendship()
centralities=centralities[0]
listt=[]
for i in range(1,len(path)):
    tup=((path[i-1]),(path[i]))
    listt.append(centralities[tup])
    plt.axvline(x=centralities[tup],color='red',linestyle='--')