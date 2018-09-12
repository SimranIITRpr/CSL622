"""
Name: Ganesh Prasad - 2018csm1008
enrolment number: Assignment: 4

Derived n Communities by removing edges with high betweenness

run:

> python Assignment_4_2018csm1008.py
"""

import networkx as nx
import matplotlib.pyplot as plt

def compute_betweenness(G):
	
	# dictionary to contain betweenness for every edge
	all_betweenness = {}

	for edge in G.edges():
		betweenness = 0
		for node1 in G.nodes():
			for node2 in G.nodes():
				if node1 < node2:
					num_of_path_via_edge = 0
					paths = list(nx.all_shortest_paths(G,node1,node2))
					for path in paths:
						if edge[0] in path and edge[1] in path:
							num_of_path_via_edge+=1
					ratio = float(num_of_path_via_edge)/len(paths)
					betweenness+=ratio
		all_betweenness[edge] = betweenness	
	all_betweenness = sorted((value,key) for key,value in all_betweenness.items())
	return all_betweenness

def community_karate(num_of_comm = 2):
	G = nx.karate_club_graph()
	#G = nx.read_weighted_edgelist(r"zachary.txt",create_using=nx.Graph(), nodetype = int)

	plt.figure("Initial state")
	nx.draw(G, with_labels = True)


	print("\nremoved edges:\n")
	while(len(list(nx.connected_components(G))) < num_of_comm):
		all_betweenness = compute_betweenness(G) 
		betweenness, edge = all_betweenness.pop()
		G.remove_edge(*edge)
		print(edge)
	fig_name = "Final state : " + str(num_of_comm) + " communities"
	plt.figure(fig_name)
	nx.draw(G,with_labels = True, node_color = 'b')
	plt.show()

if __name__ == "__main__":
	try:
		number_of_comm = int(input("Enter number of communities to create: (*Press Enter for default) "))
	except ValueError:
		number_of_comm = 2
	community_karate(number_of_comm)
