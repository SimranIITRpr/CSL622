#Assignment No. 4
#Name : A.Mamatha
#Entry No. 2014CSb1006
#Finding the communities

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community
import random
import sys

G=nx.Graph()  # Production of Graph
# G.add_nodes_from([1,2,3,4,5,6,7])
# G.add_edges_from([(1,4),(1,6),(4,6),(3,6),(4,3),(5,6),(5,7),(5,2),(7,2),(1,5),(3,5)])
G=nx.karate_club_graph() # Reading the network 


def betweenness(G):	 	 # function to compute the edge betweenness of a graph
	dictionary={}   	 # creating a dictionary 
	E = list(G.edges())  # E contains the list of all edges
	V = list(G.nodes())  # V contains the list of all nodes 
	for i in range(G.number_of_edges()):
		edge = frozenset(E[i])  # frozenset() to return the edge touple
		dictionary[edge]=0.0 
	for node1 in V:
		for node2 in V:
			shortestPath_n1n2 = list(nx.all_shortest_paths(G, node1, node2))# finding all shortest paths
			allShortestPaths = float(len(shortestPath_n1n2))                # list of all shortest paths
			 												                # shortest path between node1 and node2
																			# length of the shortest path
			for i in shortestPath_n1n2:
				for j in range(len(i)-1):
					if i[j] != i[j+1]:
						edge = frozenset([i[j], i[j+1]])
						dictionary[edge] += 1.0/allShortestPaths
	return dictionary 

while (nx.is_connected(G)==True):
	D=betweenness(G)       					# calling the betweenness function
	#print D
	Y= max(D.keys(), key=(lambda k: D[k]))  # finding the edge with maximum bridgyness
	print Y									# Showing the edges or labels or tuples which are being removed
	G.remove_edge(*Y)						# Removing the edge with maximum bridgyness
nx.draw(G, with_labels=1)					# Draw the graph with labels
plt.show(G)									# Display the graph