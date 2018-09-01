"""
@author: Subhranil Bagchi
Entry Number: 2018CSY0002
"""

"""
Quickest Propanant in a graph- the quickest propanant in a graph will be the nodes that lie
at the centre of the graph. This is what our algorithm aims to do. This algorithm is more suitable
for a sparse graph, unlike this one.
"""

import networkx as netx
import matplotlib.pyplot as plt
G = netx.read_edgelist("pagerank.txt",create_using=netx.DiGraph(),nodetype=int)
netx.draw_spring(G,with_labels=1,node_size=200,font_size=12)
plt.show()
max_pathLen = 0
farthest_sourcelist = []
farthest_source = []
for eachNode in G.nodes():
    for eachOtherNode in G.nodes():
        if (eachNode!=eachOtherNode):
            if (netx.has_path(G,source=eachNode,target=eachOtherNode)):
                farthest_source.append(eachNode)
                path_len = netx.shortest_path_length(G, source=eachNode, target = eachOtherNode)
                if path_len>max_pathLen: 
                    max_pathLen = path_len
                    farthest_sourcelist = farthest_source
                if path_len==max_pathLen:
                    farthest_sourcelist.append(farthest_source[0])
quickest_propanant = []
for item in farthest_sourcelist:
    for eachDest in G.nodes():
        if (item!=eachDest):
            path_len = netx.shortest_path_length(G, source=item, target=eachDest)
            if path_len==int(max_pathLen/2):
                quickest_propanant.append(eachDest)
quickest_propanant = list(set(quickest_propanant))
print(quickest_propanant)