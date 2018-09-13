#===========================================================================
"""
Assignment 4 : "Community detection by using edge betweenness centrality" 


Submitter : Amit Kumar Chauhan (2017csz0008) 

"""
#===========================================================================

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import operator


G = nx.karate_club_graph()
nodes = G.nodes()
edges = G.edges()

N_COMP = 2

def fn(G):
    """returns edge betweeness"""
    nodes = G.nodes()
    edges = G.edges()
    # initialize an empty dictionary to store edge betweeness
    edge_betweeness_pairs = {}
    for edge in edges:
        edge_betweeness_pairs[edge] = 0.0
    # print(edge_betweeness_pairs)


    # make a list of all the shortest paths of the graph
    shortest_path_list=[]
    for node1 in nodes:
        for node2 in nodes:
            if(node1 != node2):
                shortest_path=list(nx.all_shortest_paths(G, node1, node2))
                shortest_path_list.append(shortest_path)
    # print(shortest_path_list)            
                
    # simplified (for easy calculation later) list of all the shortest paths
    path_list = []
    for path in shortest_path_list:
        for i in path:
            path_list.append(i)
    # print(path_list)

 

    # Edge betweeness: fraction of shortest paths between all pairs of vertices passing through that edge.
    for edge in edges:
        xcount = 0
        for path in path_list:
            for i in range(len(path) - 1):
                if edge[0] == path[i] and edge[1] == path[i + 1]:
                    xcount += 1
        edge_betweeness_pairs[edge] = xcount / len(path_list)
        

    #sort edges based on the betweeness
    sorted_betweenness = list(sorted(edge_betweeness_pairs.items(), key=operator.itemgetter(1),reverse=True))
    return sorted_betweenness

edge_betweeness_pairs = fn(G)
    
# print("Edge betweeness:\n", edge_betweeness_pairs)


G_copy = G.copy()

while len(G_copy) > 1:
    edge_betweeness_pairs = fn(G_copy) # calculate edge_betweeness again
    i = edge_betweeness_pairs[0] # first edge (having highest betweenness)
    s = i[0][0]
    t = i[0][1]
    # remove the edge with highest betweenness
    G_copy.remove_edge(s, t)
    print('Edge removed: '+"("+str(s)+","+str(t)+")"+" and betweenness is "+str(i[1]))
    # check if graph connected
    if (not nx.is_connected(G_copy)):
        subgraphs = list(nx.connected_component_subgraphs(G_copy, copy=False))
    # check if no of components is as specified earlier
    if(N_COMP==nx.number_connected_components(G_copy)):
        plt.figure("Components of graph after Removing edges")
        nx.draw(G_copy,with_labels = True)
        plt.show()
        break
 
#===========================================================================

