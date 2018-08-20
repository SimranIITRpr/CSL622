#Collaborators- Harsimar Singh, Subhranil Bagchi, Anurag Banerjee

#In this module we will find the weak link and then make it a strong
#link in the graph and it is similar to the increasing influence
#of a newly created website.
#Given graph is undirected 


import networkx as nx
import matplotlib.pyplot as plt
import random

#find the weak link in Graph
def weak_link(Graph): 
	#degree.values() function doesn't work 
	degrees = [val for (node, val) in G.degree()] 
	nodes = [val for (val) in G.nodes()]
	print(min(degrees))
	weak_degree=min(degrees)
	list_nodes_weak=[]
	for i in nodes:
		if G.degree[i]==weak_degree:
			list_nodes_weak.append(i)
	print(list_nodes_weak)	
	weak_node=random.choice(list_nodes_weak)
	return (weak_node)	

#find the strongest link in graph
def leader(Graph):
	#degree.values() function doesn't work 

	degrees = [val for (node, val) in G.degree()] 
	nodes = [val for (val) in G.nodes()]
	list_leader=[]
	
	for i in nodes:
		if G.degree[i]==max(degrees):
			list_leader.append(i)
	print(list_leader)
	leader_node=random.choice(list_leader)
	return (leader_node)	

#add edges in the graph to make the weak link a strongest one
def connect(G,weak,leader):
	neighbour=[]
	neighbour=G.neighbors(leader)
	for i in neighbour:
		G.add_edge(weak,i)

G=nx.read_edgelist('DATASET/pagerank.txt')

weak=weak_link(G)

print ("degree of weak node is " + str(G.degree(weak) ))

leader=leader(G)

connect(G,weak,leader)

print (G.degree())
print ("degree of weak node after connecting to neighbour of leader node is " + str(G.degree(weak)))		
