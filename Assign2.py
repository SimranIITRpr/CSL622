# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 19:31:17 2018

@author: Simran Setia (2017csz0001) and Amanjot Kaur(2017csz0014)

This function calculates the prospective friends of less impressive person

Steps. First of all, we calculated the pagerank values and find out least 
impressive person. Then we calculated the prospective friends of least impressive
 person using Triadic Closure Property. Had he met these prospective friends,he wouldn't
 have been the least impressive person.
"""

import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_edgelist(r"C:\Users\hi\Desktop\pagerank.txt",create_using=nx.Graph(), nodetype = int)
nx.draw(G)
'''Page Rank calculation'''
pr = nx.pagerank(G, alpha=0.9)
plt.show()
u=min(pr.values())
print(u)
for j in pr.keys():
    if(pr[j]==u):
        print(j)
        break
'''Calculation of prospective friends'''
temp=[]
for i in G.neighbors(j):
    for x in G.neighbors(i):
        if G.has_edge(j,x)==False:
            if(x!=j and x not in temp):
                temp.append(x)
print(temp)
            
