# CSL622 Assignment 1
# Abhishek Singh (2016csb1028)
# Yashwant Sihara (2016csb1065)
# Predicts susceptibility to suicide

import networkx as nx 
import matplotlib.pyplot as plt 
#take the graph as an input
G=nx.read_edgelist('pagerank.txt')
#store the nodes and their clustering coefficient in this dictionary
nodes_cluster_coef={}
#for each node:
for i in list(G.node()):
	#neighbor of current node
	neigh_nodes=list(G.neighbors(i))
	#counts total number of friendships within the neighbor
	count_friendship=0
	for j in neigh_nodes:
		for k in list(G.neighbors(j)):
			if k in neigh_nodes:
				count_friendship+=1
	#divide by 2 because one friendship is counted twice.
	count_friendship=count_friendship/2
	all_possible=(float(len(neigh_nodes)*(len(neigh_nodes)-1))/2)
	ratio=((float)(count_friendship))/all_possible
	nodes_cluster_coef[i]=ratio

print "Nodes in decreasing order of susceptibility to suicide "

store=[]
#print nodes and clustering coefficient.
for i in sorted(nodes_cluster_coef.items(),key=lambda x:x[1]):
	if i[1]<0.5:
		if len(store)==0:
			store.append(i[0])
		print "Node:",i[0]," Clustur-coef:",i[1]

print "Highest Susceptibility to suicide: Node:",store[0]