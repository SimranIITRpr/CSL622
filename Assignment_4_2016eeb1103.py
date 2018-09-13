#importing packages
import networkx as nx                                      
import matplotlib.pyplot as plt
import random

#importing Zachary KArate Club Graph
G = nx.karate_club_graph()

#defining a function to compute betweenness centrality
def BetweennessCentrality(g):
	count = 0	#counter
	res = []
	mat = []
	#initializing 2D matrix with zero
	for i in xrange(len(G.nodes())):
		mat.append([])
		for j in xrange(len(G.nodes())):
			mat[i].append(0.0)
	#finding shortest path between every pair of node		
	for i in range(len(G.nodes())):	
		path = nx.single_source_shortest_path(G,i)	#function to compute shortest path
		for p in range(len(path)): 
			for k in range(len(path[p])-1):
				mat[path[p][k]][path[p][k+1]]+=1.0
		count = count+len(path)
	#finding betweenness centrality
	for i in range(len(G.nodes())):
		for j in range(len(G.nodes())):
			mat[i][j] = mat[i][j]/count

	return mat #returnin the matrix
#removing the nodes with high betweenness centrality as long as graph is connected
while(nx.is_connected(G)):
	mat = BetweennessCentrality(G)	#calling BetweennessCentrality function
	x = 0
	y = 0
	maxm = -1.0
	#finding the edge with highest betweenness value
	for i in range(len(G.nodes())):
		for j in range(len(G.nodes())):
			if(maxm < mat[i][j]):	#updating maximum value
				x = i
				y = j
				maxm = mat[i][j]
	G.remove_edge(x,y)	#removing edge with high betweenness from the graph
	
nx.draw(G,with_labels=1)	# Drawing the graph with labels
plt.show()					# Printing the graph
