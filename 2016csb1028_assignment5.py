import networkx as nx
import matplotlib.pyplot as plt
import pprint
with open("subj.txt") as file:
	points = [point.strip() for point in file.readlines()]
	points = {int(point.split()[0]):point.split()[1:] for point in points}
	nodes = points.keys()
G = nx.Graph()
G.add_nodes_from(nodes)
for i in range(1, len(points)):
	for j in range(i + 1, len(points)+1):
		for (flagi, flagj) in zip(points[i], points[j]):
			if flagi == '1' and flagj == '1':
				if not G.has_edge(i, j):
					G.add_edge(i, j, weight = 1)
				else:
					weight = float(1 / float(G[i][j]['weight']))
					G.remove_edge(i, j)
					G.add_edge(i,j,weight = 1 / (weight + 1))
					
for i in G.nodes():
	for j in G.nodes():
		if i != j and nx.has_path(G, i, j):
			max_overlap = nx.dijkstra_path(G, i, j)
			print "Best possible path between " + str(i) + " and " + str(j) + " is " + str(max_overlap)
