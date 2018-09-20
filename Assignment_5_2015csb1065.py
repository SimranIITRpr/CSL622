#! usr/bin/python
'''
Assignment 5

Narotam Singh 2015CSB1065

Weight for each edge is the number of common 1s among the edges.
To find the best path between any two edges : After reading the question, it seems like we 
have to implement the greedy approach and select edges with max weight at each step until 
target node is found, but this will result in cycles in some cases and if cycles are not allowed
then such a path will not exist.


So to my understanding, I have implemented the following :
For all (u,v) pairs :
    If (u,v) nodes have a direct edge between them:
        the best path is simply that edge.
    Otherwise :
        Find the paths between (u,v) nodes that have the smallest length possible (length means simply number of edges in the path and not the weights)
        Now from these paths that all have equal lengths, return the path with highest sum of weights of member edges.
        There maybe multiple paths but only one is returned.
'''

import networkx as nx
import os

cwd = os.getcwd()
file = open(cwd + '\subj.txt', 'r')
G=nx.Graph()
dictionary_of_nodes=dict()  #dictionary to store the array of 0 and 1 for each node


#reading file line by line and constructing the dictionary to store the arrays
for line in file:
    fields = line.split()
    dictionary_of_nodes[int(fields[0])]=list(fields[1:len(fields)])
    G.add_node(int(fields[0])) #adding nodes to the graph

def check_zeroes(list1,list2):  #function to count common number of zeros
    summ=0
    for i in range(0,len(list1)):
        if(list1[i]==list2[i] and int(list1[i]) is 1):
            summ=summ+1
    return summ


#adding edges to the graph
for u in dictionary_of_nodes:
    for v in dictionary_of_nodes:
        if(u!=v):
            list1=dictionary_of_nodes[u]
            list2=dictionary_of_nodes[v]
            if(check_zeroes(list1,list2)>0 and ~(G.has_edge(u,v))):
                G.add_edge(u,v,weight=check_zeroes(list1,list2))    #adding edge to graph with weight as number of common 1s

pos=nx.spring_layout(G)
labels = nx.get_edge_attributes(G,'weight');
nx.draw(G,pos,with_labels=1)
nx.draw_networkx_edges(G,pos)
l=nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

dictionary_of_paths=dict()  #dictionary to store the shortest paths(paths with minimum length) between every pair

for u in list(G.nodes()):
    for v in list(G.nodes()):
        if(u!=v and dictionary_of_paths.get((u,v))==None and dictionary_of_paths.get((v,u))==None):
            if(G.has_edge(u,v)):
                dictionary_of_paths[(u,v)]=[[u,v]]  #if there is a single edge then consider it best
            else:
                #if there are multiple paths then store all of them
                paths=[p for p in nx.all_shortest_paths(G,u,v)] #this function considers each edge's weight as 1 (default). To find the length, we dont need to consider the weights(as we defined above).
                dictionary_of_paths[(u,v)]=paths


#print the path that has the max sum of weights. This path is the best path
for item in dictionary_of_paths:
    maxx=-1
    ans=[]
    for p in dictionary_of_paths[item]:
        summ=0
        for i in range(0,len(p)-1):
            summ=summ+G[p[i]][p[i+1]]['weight']
        if(summ>maxx):
            maxx=summ
            ans=p
    print(item," : ",ans)
        




