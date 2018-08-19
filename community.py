# -*- coding: utf-8 -*-
"""
Spyder Editor
By Simran(2017csz0001) and Amanjot(2017csz0014)

This is a temporary script file.
"""
import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_edgelist(r"C:\Users\hi\Desktop\pagerank.txt",create_using=nx.Graph(), nodetype = int)
nx.draw(G)

plt.show()


print(nx.edge_betweenness_centrality(G))

for i in range(30):
        l=[]
        l=list(nx.edge_betweenness_centrality(G).values())
        item=l[0]
        maxi=item
        for item in nx.edge_betweenness_centrality(G).values():
            if(maxi<item):
                maxi=item
                for j in nx.edge_betweenness_centrality(G).keys():
                    if(nx.edge_betweenness_centrality(G)[j]==maxi):
                        print(j)
                        break
        if(G.has_edge(*j)):
            G.remove_edge(*j)
        nx.draw(G,with_labels=1)
        plt.show()
