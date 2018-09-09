"""
get the min distance from all the pairs of nodes and 
then go for the nodes which are farthest from each other
(diameter of the graph)

"""

"""

@author: Vishal Singh(2015csb1040), Sonu(2015csb1034) 
"""
"""
function name 
returns the longest friendship possible in the group
"""
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
    nx.draw(G,pos,node_color='k',with_labels=1)
    # draw path in red
    path = nx.shortest_path(G,source=n1,target=n2)
    nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
    plt.show()
    return path

p = longest_friendship()

#%%