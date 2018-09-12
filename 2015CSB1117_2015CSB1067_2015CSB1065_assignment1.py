#! /usr/bin/python
import networkx as nx
import matplotlib.pyplot as plt
# 2015CSB1117 - Shubham Dham, 2015CSB1067 - Nittin Singh, 2015CSB1065 - Narotam Singh
# Node centrality
def centralityNodeMeasure():
    # 2015CSB1117 - Shubham Dham, 2015CSB1067 - Nittin Singh, 2015CSB1065 - Narotam Singh
    G = nx.read_adjlist('pagerank.txt',nodetype = int,create_using = nx.DiGraph())
    centralities = []
    centralities.append(nx.betweenness_centrality(G))
    diction = centralities[0]
    key, value = max(diction.items(), key = lambda x:x[1])
    color_map = []
    for node in G:
        if node == key:
            color_map.append('r')
        else:
            color_map.append('b')
    nx.draw(G,node_color = color_map, with_labels =1)
    plt.show()
    return key
centralityNodeMeasure()
