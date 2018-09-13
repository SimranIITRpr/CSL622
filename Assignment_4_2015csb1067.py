# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 16:11:11 2018

@author: nittin pc
"""
import networkx as nx
import matplotlib.pyplot as plt
import operator
# the get_edge_betweenness function calculates the edge betweenness from scratch the only inbuilt function being used is the 
# function which returns all the shortest paths available in between two nodes in  graph            
# the function get_edge_betweenness takes input the graph G and returns the dictionary with keys as edges and the value as its betweenness 
def get_edge_betweenness(G):
    
    l = {}
    for edge in list(G.edges()):
        btwn = 0
        for ii in list(G.nodes()):
            for jj in list(G.nodes()):
                if(ii!=jj and nx.has_path(G,ii,jj)):
                    lst = list(nx.all_shortest_paths(G,ii,jj))
                    counter = 0
                    for i in range(0,len(lst),1):
                        for j in range(0,len(lst[i])-1,1):
                            if(lst[i][j] == edge[0] and lst[i][j+1] == edge[1]):
                                counter += 1
                                continue
                            
                    btwn += counter/len(lst)
                    
                    
        l[edge] = btwn
    
    return l
           
G = nx.karate_club_graph()

# finding communities in the network
if nx.is_connected(G):
    print('The Graph is connected')
while(nx.is_connected(G)):
    l = get_edge_betweenness(G)
    key_edge = max(l.items(), key=operator.itemgetter(1))[0]  
    print('Removing edge:',key_edge)
    G.remove_edge(key_edge[0],key_edge[1])
print('The graph is not connected now')
communities = list(nx.connected_component_subgraphs(G))    
print('Community 1:',communities[0].nodes())
print('Community 2:',communities[1].nodes())

