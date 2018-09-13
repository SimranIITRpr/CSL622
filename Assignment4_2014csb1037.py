import networkx as nx
from collections import Counter
import itertools
import matplotlib.pyplot as plt
#function to return the edge with most edge betweenness value
def edge_betweenness_centrality(G):
    a=[]
    for x in itertools.combinations(G.nodes,2):
        for p in nx.all_shortest_paths(G,source=x[0],target=x[1]):
#appending all the edges to a which are in the shortest paths
           for c in range(len(p)-1):
             a.append((p[c],p[c+1]))
#counting all the elements repeated in a
    pr=Counter(a)
#sorting
    par=list(sorted(pr, key=pr.__getitem__,reverse=True))
    return par[0]
G=nx.karate_club_graph()
def girvan(G):
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
c=girvan(G)
#printing the nodes present in each community
for i in c:
    print (i.nodes())