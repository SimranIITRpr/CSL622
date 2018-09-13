#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 23:03:26 2018

@author: simransetia
"""
import operator 
import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
#G=nx.read_gml('/home/lab/Desktop/karate.gml')
G=nx.karate_club_graph()
#G=nx.gnp_random_graph(5,0.8)

def edge_bet(G):
    dict_edges={}
    for each in G.edges():
            dict_edges[each]=0
    list_edges=[]
    total_path=0
    for i in range(G.number_of_nodes()):
            for j in range(G.number_of_nodes()):
                    if(i!=j):
                            x=list(nx.all_shortest_paths(G,i,j))
                            #print(x)
                            total_path=total_path+len(x)
                            for item in dict_edges.keys():
                                    list_edges=list(item)
                                    for m in range(len(x)):
                                        for n in range(len(x[m])-1):
                                            if((x[m][n]==list_edges[0] and x[m][n+1]==list_edges[1]) or (x[m][n]==list_edges[1] and x[m][n+1]==list_edges[0])):
                                                    dict_edges[item]=dict_edges[item]+(1/len(x))
                            
    return dict_edges                                                




while(nx.is_connected(G)):
        l=[]
        dict_edges1=edge_bet(G)
        l=list(dict_edges1.values())
        item=l[0]
        maxi=item
        for item in dict_edges1.values():
            if(maxi<item):
                maxi=item
                for j in dict_edges1.keys():
                    if(dict_edges1[j]==maxi):
                        print(j)
                        break
        
        if(G.has_edge(*j)):
            G.remove_edge(*j)
       
        nx.draw(G,with_labels=1)
        plt.show()
