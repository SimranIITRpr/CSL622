import networkx as nx
from collections import Counter
from itertools import combinations
import matplotlib.pyplot as plt
import operator

G=nx.karate_club_graph()
#this function will return edge with most betweenes
def edge_betweenness_centrality(G):
#making an empty dictionary in which keys will be edges nad values will be number time an edge visited in shortest path    
    mydict=dict()
#making a list of all possible pair of nodes of graph     
    x=list(combinations(G.nodes(),2))
#accessing each pair of node one by one
    for y in x:
#the function in for syntax calculates all the possible shortest paths between pair of nodes and p contains sequence of nodes which depicts edges        
         for p in nx.all_shortest_paths(G,source=y[0],target=y[1]):
             n=len(p)
#finding number of nodes in p
#making sequence of edges out of these nodes and updating in dictionary if edge is alreday present then increment the value else uodate the edge with value 1             
             for i in range(0,n-1):
                 e=(p[i],p[i+1])
                 if e in mydict:
                    v=mydict.get(e)+1    
                    mydict.update({e:v})
                 else:
                      mydict.update({e:1})
#sort the dictornay in ascending order                      
    s_mydict = sorted(mydict.items(), key=operator.itemgetter(1))
#return the last key of the dictarnory after sorting
    return s_mydict[-1][0]  
def number_components(G):
#c is the number of subgraphs present in a graph g
    c=list(nx.connected_component_subgraphs(G))
    l=len(c)
    while(l==1):
#removing edges
        G.remove_edge(*edge_betweenness_centrality(G))
        c=list(nx.connected_component_subgraphs(G))
        l=len(c)
#drawing graph after we get the communities
    nx.draw(G,with_labels = True, node_color = 'b')
    plt.show()
    return c
n=number_components(G)
#printing the nodes present in each community
for i in n:
    print (i.nodes())
