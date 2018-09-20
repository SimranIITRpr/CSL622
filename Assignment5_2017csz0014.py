# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:46:35 2018

@author: hi
"""

import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

c=0

'''Reading Input File'''
file=open("C:/Users/hi/Desktop/subj.txt")
text=file.readlines()
for l in text:
    c=c+1
file.close()

for i in range(c):
        G.add_node(i)
        
print(G.nodes())

mat=[]

'''forming a matrix '''
graph = []
with open("C:/Users/hi/Desktop/subj.txt") as file:
    o = []
    o = [ line.split() for line in file ] 
    for i in range(14):
        r=[]
        for j in range(12):
            r.append(o[i][j])
        mat.append(r)

print(mat)
    
'''Adding edges if  there are common subjects in between the nodes'''   
for i in range(G.number_of_nodes()):
        y=i+1
        while(y<G.number_of_nodes()):
                
                for j in range(12):
                        if(mat[i][j]==mat[y][j] and mat[i][j]=='1'):
                                G.add_edge(i,y)
                y=y+1

''''Calculating weights if there is edge between 2 nodes'''
weight={}
for i in range(G.number_of_nodes()):
        y=i+1
        while(y<G.number_of_nodes()):
                count=0
                for j in range(12):
                    if(G.has_edge(i,y)):
                        count=count+1
                weight[(i,y)]=count
                weight[(y,i)]=count
                y=y+1
print(weight)

'''''finding the best path using Floyd Warshall Algorithm'''
for i in G.nodes(): 
    for j in G.nodes():
        if i!=j and nx.has_path(G,i,j):
            if G.has_edge(i,j):
                path=nx.all_shortest_paths(G,i,j)
                print("Path with common subjects is :")
                print (i,j)       
            else:
                path=nx.floyd_warshall(G)
                print("Best Path with maximum bond strength is:")
                print(i,j)
        else:
            if i!=j:
                print (i,j)

nx.draw(G,with_labels=True)
plt.show()   
