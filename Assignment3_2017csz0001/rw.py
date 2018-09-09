#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dataset used is Bitcoin Alpha trust weighted signed network
I have converted this network to unweighted directed graph
No of nodes 3783
No of edges 24,186
There are two columns in the data set. First column represents the source and the second one represents the target.
@author: simransetia
"""

import networkx as nx
import random
import operator
import matplotlib.pyplot as plt
Data = open('/Users/simransetia/Desktop/snapdata.csv', "r")
Graphtype = nx.DiGraph()

G = nx.parse_edgelist(Data, comments='t', delimiter=',', create_using=Graphtype,nodetype=int)
print(G.number_of_nodes())
#G=nx.gnp_random_graph(100,0.5,directed=True)
#nx.draw(G,with_labels=True)
#plt.show()
x=random.choice([i for i in range(G.number_of_nodes())]) #Choose the source node randomly 
print(x)
dict_counter={} #dictionary to store the count of a particular node
for i in range(G.number_of_nodes()):
        dict_counter[i]=0
dict_counter[x]=1 #increment the counter of source node
list_n=[]          
prob=random.random() #teleportation probability
for i in range(100000):
        for i in range(G.number_of_nodes()):
                if(G.has_edge(x,i)==True):  #Checking the neighbors of node x
                        list_n.append(i)              #list_n contains neighbors of node x if any
                else:
                        x=random.choice([i for i in range(G.number_of_nodes())]) #If x has no outlinks
                        continue
        if(prob<0.2):
                x=random.choice([i for i in range(G.number_of_nodes())])#If probability >0.2, next node would be chosen randomly
                dict_counter[x]=dict_counter[x]+1	
        else:
                y=random.choice(list_n) #next node is chosen from the list of neighbors of x
                dict_counter[y]=dict_counter[y]+1 #increment the counter of the node visited
                x=y #next node i.e. y would become the source node

            
p=nx.pagerank(G) 
#print(p)
#print(dict_counter)
sorted_y=sorted(p.items(), key=operator.itemgetter(1)) #sorting the page rank dictionary based on the values
sorted_x=sorted(dict_counter.items(), key=operator.itemgetter(1)) #sorting the random walk list based on the values
#print(sorted_x)
#print(sorted_y)
print(sorted_x[:10])
print(sorted_y[:10])