import networkx as nx
import matplotlib.pyplot as plt
import time

G = nx.karate_club_graph()
#G = nx.read_weighted_edgelist(r"zachary.txt",create_using=nx.Graph(), nodetype = int)
all_betweenness = {}

for edge_end_1 in G.nodes():
	for edge_end_2 in G.nodes():
		if edge_end_1 < edge_end_2 and G.has_edge(edge_end_1, edge_end_2):
			betweenness = 0
			for node1 in G.nodes():
				for node2 in G.nodes():
					if node1 < node2:
						num_of_path_via_edge = 0
						paths = list(nx.all_shortest_paths(G,node1,node2))
						for path in paths:
							if edge_end_1 in path and edge_end_2 in path:
								num_of_path_via_edge+=1
						ratio = float(num_of_path_via_edge)/len(paths)
						betweenness+=ratio
			all_betweenness[(edge_end_1,edge_end_2)] = betweenness	

all_betweenness = sorted((value,key) for key,value in all_betweenness.items())

while(len(list(nx.connected_components(G))) < 2):
	betweenness, edge = all_betweenness.pop()
	G.remove_edge(*edge)
nx.draw(G,with_labels = True)
plt.show()
